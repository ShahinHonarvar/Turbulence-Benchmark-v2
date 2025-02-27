import string

def if_contains_anagrams(lst):
    anagrams = set()
    for s in lst:
        t = ''.join(sorted(s.lower())).translate(str.maketrans('', '', string.punctuation))
        if len(t) < 3:
            continue
        if t in anagrams:
            return True
        anagrams.add(t)
    return len(anagrams) > 36