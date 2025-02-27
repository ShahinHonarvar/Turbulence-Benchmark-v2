from collections import defaultdict

def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_counts = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            normalized = normalize(s)
            anagram_counts[normalized] += 1
    pairs = sum((v * (v - 1) // 2 for v in anagram_counts.values()))
    return pairs >= 277