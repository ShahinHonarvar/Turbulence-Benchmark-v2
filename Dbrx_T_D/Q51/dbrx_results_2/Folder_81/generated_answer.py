import string

def if_contains_anagrams(lst):
    anagrams = set()
    for s in lst:
        s = s.lower()
        sorted_s = ''.join(sorted(s))
        if len(s) >= 3 and sorted_s not in anagrams and all((c in string.ascii_letters for c in s)):
            anagrams.add(sorted_s)
    return len(anagrams) <= 79