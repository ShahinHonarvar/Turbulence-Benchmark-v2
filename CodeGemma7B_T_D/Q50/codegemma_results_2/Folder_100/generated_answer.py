from itertools import permutations

def if_contains_anagrams(str_list):
    str_list = [s.lower() for s in str_list]
    anagram_pairs = 0
    for str1 in str_list:
        for str2 in str_list:
            if str1 != str2 and sorted(str1) == sorted(str2) and (len(str1) >= 3):
                anagram_pairs += 1
    return anagram_pairs >= 95