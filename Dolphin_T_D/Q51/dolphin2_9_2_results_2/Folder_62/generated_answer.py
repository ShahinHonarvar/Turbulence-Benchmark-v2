from collections import Counter

def if_contains_anagrams(lst):
    count = Counter(''.join(lst).lower())
    res = 0
    for key in count:
        if len(key) >= 3 and key.isalpha():
            res += count[key] * (count[key] - 1) // 2
    return res <= 289