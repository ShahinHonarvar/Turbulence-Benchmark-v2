from collections import Counter

def if_contains_anagrams(lst):
    c = Counter()
    res = []
    for word in lst:
        if len(word) >= 3:
            anagram = ''.join(sorted(word.lower()))
            c[anagram] += 1
    for key in c:
        if c[key] > 1:
            res.append(c[key])
    if len(res) >= 49:
        return True
    else:
        return False