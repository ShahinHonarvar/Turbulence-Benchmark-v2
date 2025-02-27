from collections import Counter

def if_contains_anagrams(string_list):
    normalized_strings = [''.join(sorted(s.lower())) for s in string_list if len(s) >= 3]
    counts = Counter(normalized_strings)
    anagram_pairs = sum((count * (count - 1) // 2 for count in counts.values()))
    return anagram_pairs >= 153