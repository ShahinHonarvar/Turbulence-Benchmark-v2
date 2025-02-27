from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_count = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            sorted_str = ''.join(sorted(string.lower()))
            anagram_count[sorted_str] += 1
    pairs_count = sum((v * (v - 1) // 2 for v in anagram_count.values()))
    return pairs_count <= 147