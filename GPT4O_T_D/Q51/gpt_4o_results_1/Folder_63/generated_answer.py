from collections import defaultdict

def if_contains_anagrams(strings):
    normalized_strings = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    anagram_groups = defaultdict(int)
    for ns in normalized_strings:
        anagram_groups[ns] += 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_groups.values() if count > 1))
    return anagram_pairs <= 423