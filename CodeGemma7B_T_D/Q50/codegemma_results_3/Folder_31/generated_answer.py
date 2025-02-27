from itertools import combinations

def if_contains_anagrams(str_list):
    str_list = [word.lower() for word in str_list]
    str_list = [word for word in str_list if len(word) >= 3]
    anagrams = [sorted(word) for word in str_list]
    anagram_dict = {}
    for anagram in anagrams:
        if anagram in anagram_dict:
            anagram_dict[anagram] += 1
        else:
            anagram_dict[anagram] = 1
    return sum([value for value in anagram_dict.values() if value >= 2]) >= 68