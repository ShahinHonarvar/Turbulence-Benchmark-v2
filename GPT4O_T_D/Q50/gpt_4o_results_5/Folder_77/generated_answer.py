from collections import defaultdict

def if_contains_anagrams(strings):
    pairs = 0
    anagram_groups = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            normalized = ''.join(sorted(s.lower()))
            anagram_groups[normalized] += 1
    for count in anagram_groups.values():
        pairs += count * (count - 1) // 2
        if pairs >= 209:
            return True
    return False