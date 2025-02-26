from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_groups = defaultdict(list)
    for s in strings:
        cleaned = ''.join((c.lower() for c in s if c.isalpha()))
        if len(cleaned) >= 3:
            sorted_chars = ''.join(sorted(cleaned))
            anagram_groups[sorted_chars].append(s)
    anagram_pairs = sum((len(group) * (len(group) - 1) // 2 for group in anagram_groups.values()))
    return anagram_pairs <= 49