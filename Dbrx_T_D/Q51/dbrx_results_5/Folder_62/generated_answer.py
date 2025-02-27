import string

def if_contains_anagrams(lst):
    anagrams = set()
    count = 0
    for s in lst:
        s = s.lower()
        s = ''.join(sorted(s))
        if len(s) < 3:
            continue
        if s in anagrams:
            count += 1
            if count > 289:
                return False
        else:
            anagrams.add(s)
    return True