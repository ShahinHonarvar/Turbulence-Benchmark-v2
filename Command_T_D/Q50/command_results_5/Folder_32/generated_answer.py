import collections

def if_contains_anagrams(s):
    anagrams = collections.Counter(s)
    d = {}
    for k, v in anagrams.items():
        d[k] = v
    return len(d) >= 194