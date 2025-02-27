from collections import defaultdict

def if_contains_anagrams(strings):
    normalized_strings = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    anagram_count = defaultdict(int)
    pair_count = 0
    for ns in normalized_strings:
        pair_count += anagram_count[ns]
        anagram_count[ns] += 1
        if pair_count > 48:
            return False
    return True