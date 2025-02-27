from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_count = defaultdict(int)
    for s in strings:
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s.lower()))
        anagram_count[sorted_s] += 1
    total_pairs = sum((v * (v - 1) // 2 for v in anagram_count.values()))
    return total_pairs >= 72