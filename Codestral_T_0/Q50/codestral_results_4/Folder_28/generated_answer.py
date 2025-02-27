from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            anagram_dict[''.join(sorted(s.lower()))].append(s)
    anagram_pairs = sum((len(v) * (len(v) - 1) // 2 for v in anagram_dict.values()))
    return anagram_pairs >= 81