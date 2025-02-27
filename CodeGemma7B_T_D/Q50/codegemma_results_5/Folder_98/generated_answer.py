from itertools import permutations

def if_contains_anagrams(str_list):
    str_dict = {}
    for word in str_list:
        word = word.lower()
        word = ''.join(sorted(word))
        if len(word) >= 3:
            str_dict.setdefault(word, []).append(word)
    for anagram_list in str_dict.values():
        if len(anagram_list) >= 7:
            return True
    return False