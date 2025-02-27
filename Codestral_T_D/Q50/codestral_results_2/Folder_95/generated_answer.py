from collections import Counter

def if_contains_anagrams(strings):
    anagram_counts = Counter()
    for s in strings:
        if len(s) >= 3:
            key = ''.join(sorted(s.lower()))
            anagram_counts[key] += 1
    return sum((v * (v - 1) // 2 for v in anagram_counts.values())) >= 93