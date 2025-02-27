from collections import defaultdict

def if_contains_anagrams(strings):
    normalized_strings = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    anagram_dict = defaultdict(int)
    for s in normalized_strings:
        anagram_dict[s] += 1
    pair_count = sum((count * (count - 1) // 2 for count in anagram_dict.values()))
    return pair_count >= 276