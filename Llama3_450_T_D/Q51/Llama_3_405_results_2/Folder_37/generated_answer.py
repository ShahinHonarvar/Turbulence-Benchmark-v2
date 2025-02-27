def if_contains_anagrams(string_list):
    anagram_dict = {}
    count = 0
    for string in string_list:
        string_lower = string.lower()
        if len(string_lower) < 3:
            continue
        string_sorted = ''.join(sorted(string_lower))
        if string_sorted in anagram_dict:
            anagram_dict[string_sorted].append(string_lower)
        else:
            anagram_dict[string_sorted] = [string_lower]
    for key in anagram_dict:
        value = anagram_dict[key]
        count += len(value) * (len(value) - 1) // 2
        if count > 206:
            return False
    return True