import string

def if_contains_anagrams(strings):
    anagrams = set()
    for s in strings:
        sorted_s = ''.join(sorted(s.lower())).strip(string.punctuation)
        if len(sorted_s) >= 3:
            anagrams.add(sorted_s)
    return len(anagrams) <= 38