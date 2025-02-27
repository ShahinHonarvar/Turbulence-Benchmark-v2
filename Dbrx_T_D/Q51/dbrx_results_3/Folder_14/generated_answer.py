import string

def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        t = ''.join((c.lower() for c in s if c not in string.punctuation))
        if len(t) < 3:
            continue
        sorted_t = tuple(sorted(t))
        if sorted_t not in anagrams:
            anagrams[sorted_t] = set()
        anagrams[sorted_t].add(t)
    pair_count = sum((len(anagrams[sorted_t]) // 2 for sorted_t in anagrams.keys()))
    return pair_count <= 474