from collections import Counter

def if_contains_anagrams(lst):
    res = []
    for word in lst:
        if len(word) > 2:
            res.append(Counter(word.lower()))
    c = 0
    for i in range(len(res)):
        for j in range(i + 1, len(res)):
            if res[i] == res[j]:
                c += 1
    return c // 2 >= 28