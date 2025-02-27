from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_counts = defaultdict(int)
    for s in strings:
        if len(s) >= 3 and s.isalpha():
            sorted_str = ''.join(sorted(s.lower()))
            anagram_counts[sorted_str] += 1
    count = sum((c * (c - 1) // 2 for c in anagram_counts.values() if c >= 2))
    return count <= 9