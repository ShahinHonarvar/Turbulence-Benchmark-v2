from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_groups = defaultdict(int)
    for s in strings:
        normalized = ''.join(sorted((c.lower() for c in s if c.isalpha())))
        if len(normalized) >= 3:
            anagram_groups[normalized] += 1
    pairs = 0
    for count in anagram_groups.values():
        if count > 1:
            pairs += count * (count - 1) // 2
            if pairs > 24:
                return False
    return True