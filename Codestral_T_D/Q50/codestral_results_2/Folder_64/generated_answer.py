from collections import Counter

def if_contains_anagrams(strings):
    anagram_count = Counter()
    for s in strings:
        if len(s) >= 3:
            anagram_count[tuple(sorted(s.lower()))] += 1
    return sum((v * (v - 1) // 2 for v in anagram_count.values())) >= 5