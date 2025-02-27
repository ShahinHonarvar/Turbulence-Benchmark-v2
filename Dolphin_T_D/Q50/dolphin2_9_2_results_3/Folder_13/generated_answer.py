from collections import Counter

def if_contains_anagrams(lst):
    cnt = Counter()
    for word in lst:
        if len(word) >= 3:
            cnt[tuple(sorted(word.lower()))] += 1
    for v in cnt.values():
        if v >= 144:
            return True
    return False