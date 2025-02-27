from collections import Counter

def if_contains_anagrams(lst):
    c = Counter()
    for word in lst:
        if len(word) >= 3:
            c[''.join(sorted(word.lower()))] += 1
    return 24 <= sum((v * (v - 1) // 2 for v in c.values().values()))