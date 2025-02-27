from collections import Counter

def if_contains_anagrams(strings):
    anagram_counts = {}
    for s in strings:
        s = s.lower()
        if len(s) < 3:
            continue
        count = Counter(s)
        signature = tuple(sorted(count.items()))
        if signature in anagram_counts:
            anagram_counts[signature] += 1
        else:
            anagram_counts[signature] = 1
    return sum((c * (c - 1) // 2 for c in anagram_counts.values())) >= 20