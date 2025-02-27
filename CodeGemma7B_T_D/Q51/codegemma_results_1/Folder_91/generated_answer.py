def if_contains_anagrams(str_list):
    anagram_dict = {}
    for string in str_list:
        sorted_string = ''.join(sorted(string.lower()))
        if sorted_string in anagram_dict:
            anagram_dict[sorted_string] += 1
        else:
            anagram_dict[sorted_string] = 0
    for count in anagram_dict.values():
        if count > 3:
            if count * (count - 1) // 2 > 88:
                return False
    return True