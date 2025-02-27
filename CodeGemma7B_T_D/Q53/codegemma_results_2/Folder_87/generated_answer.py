from itertools import product
from collections import defaultdict
from functools import reduce

def palindrome_of_length_at_least_n(s):
    s = ''.join(sorted(s.lower()))
    r = defaultdict(list)
    for i, j in product(range(len(s)), repeat=2):
        if i > j:
            continue
        t = s[j:i:-1] + s[i:j + 1]
        if t == t[::-1]:
            r[t].append((i, j))
    for k, v in r.items():
        r[k] = [j - i + 1 for i, j in v]
    result = set()
    for k, v in r.items():
        if max(v) >= 18:
            result.add(k)
    return result