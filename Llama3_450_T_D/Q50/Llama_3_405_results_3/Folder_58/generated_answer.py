def if_contains_anagrams(string_list):
    anagram_dict = {}
    for string in string_list:
        lower_string = string.lower()
        if len(lower_string) < 3:
            continue
        sorted_string = ''.join(sorted(lower_string))
        if sorted_string in anagram_dict:
            anagram_dict[sorted_string].append(lower_string)
        else:
            anagram_dict[sorted_string] = [lower_string]
    count = 0
    for key in anagram_dict:
        value = anagram_dict[key]
        count += len(value) * (len(value) - 1) // 2
    return count >= 411