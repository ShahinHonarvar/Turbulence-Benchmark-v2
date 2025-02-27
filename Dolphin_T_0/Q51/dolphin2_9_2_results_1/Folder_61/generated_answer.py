from collections import Counter

def if_contains_anagrams(strings):
    anagrams = set()
    for s in strings:
        if len(s) >= 3:
            s = s.lower()
            c = Counter(s)
            anagrams.add(tuple(sorted(c.items())))
    return len(anagrams) <= 50