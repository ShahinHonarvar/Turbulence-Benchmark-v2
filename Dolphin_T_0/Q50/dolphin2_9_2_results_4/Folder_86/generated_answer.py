from collections import Counter
    from itertools import combinations

def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return Counter(s1.lower()) == Counter(s2.lower())
    pairs_count = 0
    for comb in combinations(lst, 2):
        if is_anagram(comb[0], comb[1]) and len(comb[0]) >= 3 and (len(comb[1]) >= 3):
            pairs_count += 1
    if pairs_count >= 115:
        return True
    else:
        return False