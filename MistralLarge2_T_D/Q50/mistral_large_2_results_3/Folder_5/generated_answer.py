from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_count = defaultdict(int)
    strings = [s.lower() for s in strings if len(s) >= 3]
    for s in strings:
        sorted_s = ''.join(sorted(s))
        anagram_count[sorted_s] += 1
    pairs_count = sum((count * (count - 1) // 2 for count in anagram_count.values()))
    return pairs_count >= 21