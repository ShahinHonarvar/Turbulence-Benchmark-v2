from collections import Counter

def if_contains_anagrams(lst):
    anagrams = 0
    for s1 in lst:
        if len(s1) >= 3:
            for s2 in lst:
                if s1 != s2 and len(s2) >= 3:
                    if Counter(s1.lower()) == Counter(s2.lower()):
                        anagrams += 1
                        if anagrams >= 8:
                            return True
    return False