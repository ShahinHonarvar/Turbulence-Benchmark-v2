from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(set)
    for string in strings:
        canonical_form = ''.join(sorted(string.lower()))
        if len(canonical_form) >= 3:
            anagram_dict[canonical_form].add(string)
    anagram_pairs = sum((len(v) * (len(v) - 1) // 2 for v in anagram_dict.values()))
    return anagram_pairs <= 73