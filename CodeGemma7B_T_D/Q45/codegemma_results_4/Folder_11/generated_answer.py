from collections import defaultdict

def palindromes_between_indices(word):
    d = defaultdict(list)
    for i, c in enumerate(word):
        if 'a' <= c.lower() <= 'z':
            d[c.lower()].append(i)
    if len(d) < 4:
        return set()
    ans = set()
    combine(word, d['a'], 0)
    combine(word, d['b'], 1)
    combine(word, d['c'], 2)
    combine(word, d['d'], 3)
    return ans

def combine(word, arr, start):
    if len(arr) < start + 4:
        return
    if start + 4 == len(arr):
        ans.add(word[arr[start]:arr[start + 4] + 1])
        return
    for i in range(start + 4, len(arr)):
        word[arr[i]], word[arr[start + 4]] = (word[arr[start + 4]], word[arr[i]])
        combine(word, arr, start + 1)
        word[arr[i]], word[arr[start + 4]] = (word[arr[start + 4]], word[arr[i]])