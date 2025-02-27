from collections import Counter

def if_contains_anagrams(lst):
    res = set()
    for word in lst:
        if len(word) >= 3:
            res.add(tuple(sorted(Counter(word.lower()))))
    if len(res) > 474:
        return True
    return False