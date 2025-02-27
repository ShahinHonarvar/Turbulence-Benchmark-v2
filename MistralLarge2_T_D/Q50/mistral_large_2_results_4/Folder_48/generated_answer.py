from collections import defaultdict

def if_contains_anagrams(lst):
    counts = defaultdict(int)
    for s in lst:
        if len(s) >= 3:
            counts[''.join(sorted(s.lower()))] += 1
    anagram_pairs = sum((v * (v - 1) // 2 for v in counts.values() if v > 1))
    return anagram_pairs >= 219