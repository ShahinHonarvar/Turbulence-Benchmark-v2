from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_count = defaultdict(int)
    for s in strings:
        sorted_str = ''.join(sorted(s.lower()))
        if len(sorted_str) >= 3:
            anagram_count[sorted_str] += 1
    pair_count = sum((count * (count - 1) // 2 for count in anagram_count.values()))
    return pair_count >= 28