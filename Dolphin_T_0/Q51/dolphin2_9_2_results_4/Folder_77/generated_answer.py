from collections import Counter
    from math import comb as binomial_coefficient

def if_contains_anagrams(lst):
    anagram_pairs = 0
    strs = [''.join(sorted(s.lower())) for s in lst if len(s) >= 3]
    strs_counter = Counter(strs)
    for key in strs_counter.keys():
        anagram_pairs += binomial_coefficient(strs_counter[key], 2)
    return anagram_pairs <= 17