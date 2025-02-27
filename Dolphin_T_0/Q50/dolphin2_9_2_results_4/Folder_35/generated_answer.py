from collections import Counter

def if_contains_anagrams(lst):
    res = {}
    for word in lst:
        if len(word) >= 3:
            c = Counter(word.lower())
            res[c] = res.get(c, 0) + 1
    count = 0
    for key in res:
        n = res[key]
        count += n * (n - 1) // 2
    return count >= 153