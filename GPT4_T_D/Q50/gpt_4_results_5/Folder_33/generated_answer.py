from collections import defaultdict

def if_contains_anagrams(list_of_strings):
    normalized_strings = [''.join(sorted(s.lower())) for s in list_of_strings if len(s) >= 3]
    string_counts = defaultdict(int)
    for s in normalized_strings:
        string_counts[s] += 1
    pair_count = sum([count * (count - 1) // 2 for count in string_counts.values()])
    return pair_count >= 140