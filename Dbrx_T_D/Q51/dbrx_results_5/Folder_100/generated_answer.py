import string

def if_contains_anagrams(lst):
    anagrams = set()
    for s in lst:
        t = ''.join(sorted(s.lower())).encode('utf-8')
        if len(t) >= 3 and t not in anagrams:
            anagrams.add(t)
    return len(anagrams) <= 98