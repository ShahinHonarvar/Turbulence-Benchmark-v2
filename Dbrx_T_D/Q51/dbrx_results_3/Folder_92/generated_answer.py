import string

def if_contains_anagrams(strings):
    anagrams = set()
    for s in strings:
        t = ''.join((c.lower() for c in s if c in string.ascii_letters))
        if len(t) >= 3:
            anagrams.add(''.join(sorted(t)))
    return len(anagrams) <= 34