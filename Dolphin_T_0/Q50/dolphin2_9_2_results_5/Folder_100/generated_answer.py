from collections import Counter

def if_contains_anagrams(lst):
    res = set()
    for word in lst:
        if len(word) >= 3 and word.lower() not in res:
            res.add(word.lower())
            anagrams = [word1 for word1 in res if Counter(word1) == Counter(word)]
            if len(anagrams) > 1:
                res.difference_update(anagrams[1:])
    return len(res) >= 95