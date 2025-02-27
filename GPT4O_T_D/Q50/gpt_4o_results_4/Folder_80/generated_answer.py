from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_counts = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            anagram_counts[sorted_s].append(s)
    total_pairs = 0
    for key in anagram_counts:
        n = len(anagram_counts[key])
        if n > 1:
            total_pairs += n * (n - 1) // 2
    return total_pairs >= 19