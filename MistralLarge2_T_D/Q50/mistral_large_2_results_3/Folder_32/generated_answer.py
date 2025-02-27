from collections import defaultdict

def if_contains_anagrams(strings):
    counts = defaultdict(int)
    for s in strings:
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s.lower()))
        counts[sorted_s] += 1
    anagram_pairs = sum((count // 2 for count in counts.values() if count > 1))
    return anagram_pairs >= 194