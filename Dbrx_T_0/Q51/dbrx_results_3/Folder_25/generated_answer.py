import string

def if_contains_anagrams(strings):
    anagrams = set()
    for s in strings:
        t = ''.join(sorted(s.lower())).translate(str.maketrans('', '', string.punctuation))
        if len(t) >= 3:
            anagrams.add(t)
    return len(anagrams) <= 67