from collections import Counter
	from itertools import combinations

def if_contains_anagrams(lst):
    count = 0
    for word1, word2 in combinations(lst, 2):
        w1 = word1.lower()
        w2 = word2.lower()
        if len(w1) >= 3 and len(w2) >= 3 and (Counter(w1) == Counter(w2)):
            count += 1
        if count > 98:
            return False
    return True