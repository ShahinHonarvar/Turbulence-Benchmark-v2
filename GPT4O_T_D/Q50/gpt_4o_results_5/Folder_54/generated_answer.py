from collections import defaultdict

def if_contains_anagrams(lst):
    pairs_count = 0
    anagrams = defaultdict(int)
    for s in lst:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            pairs_count += anagrams[sorted_s]
            anagrams[sorted_s] += 1
            if pairs_count >= 74:
                return True
    return False