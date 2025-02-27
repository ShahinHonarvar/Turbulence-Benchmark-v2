def if_contains_anagrams(string_list):
    anagram_count = 0
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
    for anagrams in anagram_dict.values():
        if len(anagrams) >= 2:
            anagram_count += len(anagrams) * (len(anagrams) - 1) // 2
    return anagram_count >= 92