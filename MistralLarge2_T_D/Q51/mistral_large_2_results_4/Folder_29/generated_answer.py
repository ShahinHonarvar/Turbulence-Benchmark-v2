from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_count = defaultdict(int)
    for s in strings:
        sorted_s = ''.join(sorted(s.lower()))
        anagram_count[sorted_s] += 1
    pairs = sum((v * (v - 1) // 2 for v in anagram_count.values() if len(next((k for k in anagram_count if anagram_count[k] == v))) >= 3))
    return pairs <= 318