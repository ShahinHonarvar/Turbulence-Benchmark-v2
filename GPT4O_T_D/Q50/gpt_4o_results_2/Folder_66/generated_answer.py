from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_count = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            anagram_count[sorted_s] += 1
    pairs = 0
    for count in anagram_count.values():
        pairs += count * (count - 1) // 2
        if pairs >= 92:
            return True
    return False