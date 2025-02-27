def if_contains_anagrams(strings_list):
    string_dict = {}
    for string in strings_list:
        if len(string) < 3:
            continue
        key = ''.join(sorted(string.lower()))
        if key in string_dict:
            string_dict[key].append(string)
        else:
            string_dict[key] = [string]
    anagram_pairs = 0
    for values in string_dict.values():
        if len(values) > 1:
            anagram_pairs += len(values) * (len(values) - 1) // 2
        if anagram_pairs > 401:
            return False
    return True