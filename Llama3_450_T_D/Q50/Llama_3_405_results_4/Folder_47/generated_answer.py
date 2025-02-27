from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s.lower()))
            anagrams[sorted_str].append(s)
    anagram_pairs = sum((len(values) * (len(values) - 1) // 2 for values in anagrams.values()))
    return anagram_pairs >= 47