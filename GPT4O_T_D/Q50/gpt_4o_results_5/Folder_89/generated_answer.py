from collections import defaultdict

def if_contains_anagrams(strings):
    normalized_strings = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    anagrams = defaultdict(int)
    for s in normalized_strings:
        anagrams[s] += 1
    pairs_count = sum((count * (count - 1) // 2 for count in anagrams.values()))
    return pairs_count >= 36