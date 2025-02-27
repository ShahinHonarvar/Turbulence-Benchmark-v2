def if_contains_anagrams(str_list):
    anagram_list = []
    for string in str_list:
        sorted_string = ''.join(sorted(string.lower()))
        if sorted_string not in anagram_list:
            anagram_list.append(sorted_string)
        elif sorted_string in anagram_list and anagram_list.count(sorted_string) >= 75:
            return False
    return True