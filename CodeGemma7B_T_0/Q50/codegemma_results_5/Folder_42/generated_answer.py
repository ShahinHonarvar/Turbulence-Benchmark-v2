def if_contains_anagrams(str_list):
    anagram_dict = {}
    for string in str_list:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            anagram_dict.setdefault(sorted_string, []).append(string)
    for anagram_list in anagram_dict.values():
        if len(anagram_list) >= 233:
            return True
    return False