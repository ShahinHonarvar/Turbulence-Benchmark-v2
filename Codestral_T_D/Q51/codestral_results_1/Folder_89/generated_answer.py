from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for s in strings:
        s = s.lower()
        if len(s) >= 3:
            anagrams[''.join(sorted(s))].append(s)
    anagram_pairs = sum((len(lst) * (len(lst) - 1) // 2 for lst in anagrams.values()))
    return anagram_pairs <= 73