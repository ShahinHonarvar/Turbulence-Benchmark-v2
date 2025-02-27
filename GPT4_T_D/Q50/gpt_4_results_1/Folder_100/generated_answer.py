def if_contains_anagrams(str_list):
    anagram_dict = {}
    for string in str_list:
        sorted_str = ''.join(sorted(string.lower()))
        if sorted_str in anagram_dict:
            anagram_dict[sorted_str] += 1
        else:
            anagram_dict[sorted_str] = 1
    pair_count = 0
    for count in anagram_dict.values():
        if len(sorted_str) >= 3:
            pair_count += count // 2
    return pair_count >= 95