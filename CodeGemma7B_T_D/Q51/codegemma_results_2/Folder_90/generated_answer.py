from collections import Counter

def if_contains_anagrams(strs):
    valid_anagrams = set()
    for s in strs:
        s = ''.join(sorted(s.lower()))
        if len(s) >= 3 and s not in valid_anagrams:
            if Counter(s) in [Counter('369') + Counter(p) for p in valid_anagrams]:
                return False
            valid_anagrams.add(s)
    return True