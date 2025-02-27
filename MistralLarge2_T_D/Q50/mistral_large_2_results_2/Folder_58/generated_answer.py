from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_count = defaultdict(int)
    for s in strings:
        if len(s) < 3:
            continue
        sorted_str = ''.join(sorted(s.lower()))
        anagram_count[sorted_str] += 1
    count_pairs = sum((v * (v - 1) // 2 for v in anagram_count.values() if v > 1))
    return count_pairs >= 411