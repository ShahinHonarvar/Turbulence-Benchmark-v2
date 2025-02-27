from collections import Counter

def if_contains_anagrams(lst):
    cnt = Counter()
    for word in lst:
        word = word.lower()
        if len(word) >= 3:
            cnt[tuple(sorted(word))] += 1
    return sum((v * (v - 1) // 2 for v in cnt.values())) <= 423