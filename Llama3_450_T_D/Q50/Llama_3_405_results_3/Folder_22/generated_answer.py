from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_counts = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s.lower()))
            anagram_counts[sorted_str] += 1
    pairs = sum((count * (count - 1) // 2 for count in anagram_counts.values()))
    return pairs >= 72