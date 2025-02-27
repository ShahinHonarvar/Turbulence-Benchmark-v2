def if_contains_anagrams(str_list):
    anagram_dict = {}
    for string in str_list:
        sorted_str = ''.join(sorted(string.lower()))
        if len(sorted_str) < 3:
            continue
        if sorted_str in anagram_dict:
            anagram_dict[sorted_str] += 1
        else:
            anagram_dict[sorted_str] = 1
    anagram_count = sum((count for count in anagram_dict.values() if count > 1))
    return anagram_count <= 474