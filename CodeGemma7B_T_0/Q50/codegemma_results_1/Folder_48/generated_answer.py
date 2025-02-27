def if_contains_anagrams(str_list):
    anagram_dict = {}
    for string in str_list:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            anagram_dict.setdefault(sorted_string, []).append(string)
    return len(anagram_dict) >= 219