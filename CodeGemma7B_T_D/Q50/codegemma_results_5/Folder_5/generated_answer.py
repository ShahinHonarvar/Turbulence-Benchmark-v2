from itertools import permutations

def if_contains_anagrams(str_list):
    str_list = [s.lower() for s in str_list]
    str_list = [s for s in str_list if len(s) >= 3]
    anagram_dict = {}
    for s in str_list:
        sorted_s = ''.join(sorted(s))
        if sorted_s in anagram_dict:
            anagram_dict[sorted_s] += 1
        else:
            anagram_dict[sorted_s] = 1
    for key in anagram_dict:
        if anagram_dict[key] >= 21:
            return True
    return False