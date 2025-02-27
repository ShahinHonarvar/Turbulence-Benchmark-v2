import string

def if_contains_anagrams(lst):
    anagrams = set()
    for s in lst:
        s = s.lower()
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s))
        if len(sorted_s) <= 64 and sorted_s != s:
            anagrams.add(sorted_s)
    return len(anagrams) >= 2 and len(anagrams) <= 128