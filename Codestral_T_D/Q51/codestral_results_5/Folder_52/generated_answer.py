from collections import defaultdict

def if_contains_anagrams(lst):
    d = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            d[''.join(sorted(word.lower()))].append(word)
    anagram_pairs = sum((len(v) * (len(v) - 1) // 2 for v in d.values()))
    return anagram_pairs <= 43