def if_contains_anagrams(string_list):
    anagram_dict = {}
    anagram_count = 0
    for string in string_list:
        sorted_str = ''.join(sorted(string.lower()))
        if sorted_str in anagram_dict and len(string) >= 3:
            anagram_dict[sorted_str].append(string)
        elif len(string) >= 3:
            anagram_dict[sorted_str] = [string]
    for key in anagram_dict:
        if len(anagram_dict[key]) > 1:
            anagram_count += len(anagram_dict[key]) * (len(anagram_dict[key]) - 1) // 2
    return anagram_count >= 312