import itertools

def if_contains_anagrams(lst):
    anagram_pairs = 0
    lst_lower = [s.lower() for s in lst if len(s) >= 3]
    for i in range(len(lst_lower)):
        for j in range(i + 1, len(lst_lower)):
            if sorted(lst_lower[i]) == sorted(lst_lower[j]):
                anagram_pairs += 1
    return anagram_pairs >= 9