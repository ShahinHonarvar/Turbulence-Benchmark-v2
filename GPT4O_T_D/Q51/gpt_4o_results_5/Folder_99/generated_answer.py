from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_counts = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            sorted_chars = ''.join(sorted(s.lower()))
            anagram_counts[sorted_chars] += 1
    pair_count = sum((count * (count - 1) // 2 for count in anagram_counts.values()))
    return pair_count <= 93