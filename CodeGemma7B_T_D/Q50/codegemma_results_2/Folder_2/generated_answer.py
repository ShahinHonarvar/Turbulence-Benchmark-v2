def if_contains_anagrams(str_list):
    anagram_dict = {}
    for string in str_list:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        if sorted_string not in anagram_dict:
            anagram_dict[sorted_string] = []
        anagram_dict[sorted_string].append(string)
    for anagram_group in anagram_dict.values():
        if len(anagram_group) >= 246:
            return True
    return False