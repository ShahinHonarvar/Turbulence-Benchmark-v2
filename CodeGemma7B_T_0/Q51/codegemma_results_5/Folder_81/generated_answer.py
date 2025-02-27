def if_contains_anagrams(str_list):
    anagram_dict = {}
    for string in str_list:
        sorted_str = ''.join(sorted(string.lower()))
        if len(sorted_str) >= 3 and sorted_str not in anagram_dict:
            anagram_dict[sorted_str] = string
    return len(anagram_dict) <= 79