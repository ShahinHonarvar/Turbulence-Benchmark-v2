import string

def if_contains_anagrams(list_of_strings):
    anagrams = set()
    for s in list_of_strings:
        s = s.lower()
        sorted_s = ''.join(sorted((c for c in s if c in string.ascii_letters)))
        if len(sorted_s) >= 3:
            anagrams.add(sorted_s)
    return len(anagrams) <= 173