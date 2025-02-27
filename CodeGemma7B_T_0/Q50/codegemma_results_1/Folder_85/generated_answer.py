def if_contains_anagrams(str_list):
    anagram_dict = {}
    for string in str_list:
        sorted_str = ''.join(sorted(string.lower()))
        if len(sorted_str) >= 3:
            anagram_dict.setdefault(sorted_str, []).append(string)
    return len(anagram_dict) >= 73