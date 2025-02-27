import string

def if_contains_anagrams(strings):
    letters = set(string.ascii_lowercase)
    anagrams = set()
    count = 0
    for s in strings:
        s = s.lower()
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted((c for c in s if c in letters)))
        if sorted_s in anagrams:
            count += 1
            if count > 30:
                return False
        else:
            anagrams.add(sorted_s)
    return True