def if_contains_anagrams(s):
    return bool(s) and sum((1 for s1, s2 in zip(s, s) if len(s1) >= 3 and s1.lower() == s2.lower())) >= 67