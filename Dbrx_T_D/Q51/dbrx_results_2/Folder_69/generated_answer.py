import string

def if_contains_anagrams(strings):
    anagrams = set()
    alpha = set(string.ascii_lowercase)
    for s in strings:
        s = s.lower()
        if len(s) < 3 or len(set(s) - alpha) > 0:
            continue
        sorted_s = ''.join(sorted(s))
        anagrams.add(sorted_s)
    return len(anagrams) <= 58