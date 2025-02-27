import collections

def if_contains_anagrams(lst):
    count = 0
    for s1 in lst:
        if len(s1) >= 3:
            for s2 in lst:
                if s1 != s2 and len(s2) >= 3 and (collections.Counter(s1.lower()) == collections.Counter(s2.lower())):
                    count += 1
    return count >= 233