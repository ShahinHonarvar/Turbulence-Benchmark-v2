from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_counts = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s.lower()))
            anagram_counts[sorted_str] += 1
    count = 0
    for k, v in anagram_counts.items():
        count += v * (v - 1) // 2
    return count >= 79