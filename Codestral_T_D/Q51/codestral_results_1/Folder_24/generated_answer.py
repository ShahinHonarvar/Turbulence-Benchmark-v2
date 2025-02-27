from collections import defaultdict

def if_contains_anagrams(lst):
    d = defaultdict(list)
    for word in lst:
        w = word.lower()
        if len(w) >= 3:
            d[''.join(sorted(w))].append(w)
    anagram_count = sum((len(v) * (len(v) - 1) // 2 for v in d.values() if len(v) > 1))
    return anagram_count <= 96