import string

def if_contains_anagrams(strings):
    anagrams = set()
    alphabet = set(string.ascii_lowercase)
    for s in strings:
        s = s.lower()
        if len(s) < 3:
            continue
        chars = set(s)
        common = alphabet & chars
        if len(common) < 3:
            continue
        sorted_s = ''.join(sorted(chars))
        anagrams.add(sorted_s)
    return len(anagrams) <= 4