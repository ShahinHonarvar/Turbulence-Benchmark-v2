def if_contains_anagrams(lst):
    ans = 0
    d = dict()
    for word in lst:
        if len(word) >= 3:
            k = ''.join(sorted(word.lower()))
            if k in d:
                d[k] += 1
            else:
                d[k] = 1
            if d[k] > 1 and d[k] % 2 == 0:
                ans += 1
            elif d[k] > 2:
                ans += 1
    return ans >= 188