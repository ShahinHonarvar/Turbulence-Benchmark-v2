import string

def if_contains_anagrams(str_list):
    anagrams = set()
    for s in str_list:
        s = s.lower()
        sorted_s = ''.join(sorted(s))
        if len(sorted_s) >= 3 and sorted_s not in anagrams:
            anagrams.add(sorted_s)
    return len(anagrams) <= 88