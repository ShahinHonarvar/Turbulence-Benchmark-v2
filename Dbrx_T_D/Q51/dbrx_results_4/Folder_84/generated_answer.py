import collections

def if_contains_anagrams(lst):
    anagrams = collections.defaultdict(set)
    for s in lst:
        sorted_s = tuple(sorted((c.lower() for c in s if s.isalpha())))
        anagrams[sorted_s].add(s)
    return any((len(v) >= 3 and len(v) <= 16 for v in anagrams.values()))