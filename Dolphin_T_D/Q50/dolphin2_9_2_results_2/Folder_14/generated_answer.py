from collections import Counter

def if_contains_anagrams(lst):
    c = Counter()
    for i in range(len(lst)):
        if len(lst[i]) >= 3:
            c.update([lst[i].lower()])
    return len(c) >= 22