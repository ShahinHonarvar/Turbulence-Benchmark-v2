def if_contains_anagrams(s):
    return s.count(sorted(s)[::2]) > 400