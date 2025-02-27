def if_contains_anagrams(str_list):
    anagram_dict = {}
    for string in str_list:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        if sorted_string in anagram_dict:
            anagram_dict[sorted_string] += 1
            if anagram_dict[sorted_string] > 257:
                return False
        else:
            anagram_dict[sorted_string] = 1
    return True