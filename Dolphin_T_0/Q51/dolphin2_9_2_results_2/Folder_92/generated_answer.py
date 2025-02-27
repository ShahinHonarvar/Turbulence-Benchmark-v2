from collections import Counter

def if_contains_anagrams(lst):
    ans = 0
    m = {}
    for word in lst:
        if len(word) >= 3:
            k = ''.join(sorted(word.lower()))
            if k not in m:
                m[k] = 1
            else:
                ans += m[k]
                m[k] += 1
    return ans // 2 <= 34