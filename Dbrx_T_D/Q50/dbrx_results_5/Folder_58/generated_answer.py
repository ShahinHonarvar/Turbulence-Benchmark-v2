import string

def if_contains_anagrams(string_list):
    anagrams = set((''.join(sorted(s.lower())) for s in string_list if len(s) >= 3))
    return len(anagrams) >= 411