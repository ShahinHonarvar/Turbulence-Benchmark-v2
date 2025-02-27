from collections import defaultdict

def if_contains_anagrams(lst):
    freq = defaultdict(int)
    for s in lst:
        if len(s) >= 3:
            freq[''.join(sorted(s.lower()))] += 1
    pairs_count = 0
    for value in freq.values():
        pairs_count += value // 2
        if pairs_count > 2:
            return False
    return True