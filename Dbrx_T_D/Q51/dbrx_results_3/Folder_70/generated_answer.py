import string

def if_contains_anagrams(lst):
    anagrams = set()
    for s in lst:
        s = s.lower()
        if len(s) < 3 or not s.isalpha():
            continue
        sorted_s = ''.join(sorted(s))
        if sorted_s in anagrams:
            return True
        anagrams.add(sorted_s)
    return len(anagrams) <= 97