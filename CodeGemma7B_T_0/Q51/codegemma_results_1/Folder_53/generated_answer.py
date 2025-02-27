def if_contains_anagrams(str_list):
    anagram_dict = {}
    for string in str_list:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3 and sorted_string not in anagram_dict:
            anagram_dict[sorted_string] = string
    if len(anagram_dict) <= 8:
        return True
    else:
        return False