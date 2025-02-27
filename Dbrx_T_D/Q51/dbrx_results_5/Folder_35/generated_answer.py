import string

def if_contains_anagrams(lst):
    anagrams = set()
    for s in lst:
        sorted_s = ''.join(sorted(s.lower()))
        if len(sorted_s) < 3 or any((c in sorted_s for c in string.punctuation)):
            continue
        anagrams.add(sorted_s)
    return len(anagrams) <= 210