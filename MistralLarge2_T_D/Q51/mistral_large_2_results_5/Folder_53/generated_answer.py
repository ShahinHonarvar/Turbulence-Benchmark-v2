from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_count = defaultdict(int)
    for s in strings:
        if len(s) < 3:
            continue
        key = ''.join(sorted(s.lower()))
        anagram_count[key] += 1
    total_pairs = sum((v * (v - 1) // 2 for v in anagram_count.values()))
    return total_pairs <= 8