import string

def if_contains_anagrams(lst):
    english_letters = set(string.ascii_lowercase)
    anagrams = set()
    for s in lst:
        s = s.lower()
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted((c for c in s if c in english_letters)))
        if len(sorted_s) >= 3:
            if sorted_s in anagrams:
                return True
            anagrams.add(sorted_s)
    return False