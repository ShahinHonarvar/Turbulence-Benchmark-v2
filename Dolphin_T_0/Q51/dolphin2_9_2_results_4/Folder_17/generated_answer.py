from collections import Counter

def if_contains_anagrams(lst):
    res = set()
    for word in lst:
        if len(word) >= 3:
            c = Counter(word.lower())
            res.add(c)
    return len(res) <= 22