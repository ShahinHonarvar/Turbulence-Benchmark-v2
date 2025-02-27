def if_contains_anagrams(str_list):
    anagram_dict = {}
    for string in str_list:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3 and sorted_string in anagram_dict:
            anagram_dict[sorted_string] += 1
            if anagram_dict[sorted_string] > 25:
                return False
        else:
            anagram_dict[sorted_string] = 1
    return True