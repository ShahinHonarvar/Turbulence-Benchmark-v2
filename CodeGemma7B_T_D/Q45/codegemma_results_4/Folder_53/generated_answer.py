from itertools import permutations
    import re

def palindromes_between_indices(s):
    p = re.compile('^[A-Za-z]+$')
    if not p.match(s):
        return set()
    d = {l: 0 for l in s[4:9]}
    for letter in s[4:9]:
        d[letter] += 1
    t = sum(d.values())
    if t < 6 or t % 2 != 0:
        return set()
    key, value = next(((k, v) for k, v in sorted(d.items())))
    if value > len(s[4:9]) // 2:
        return set()
    lst = [key] * value + [k for k, v in sorted(d.items()) if k != key] * (len(s[4:9]) - value)
    result = set()
    for i in permutations(lst):
        s = ''.join(i)
        if s == s[::-1] and len(s) >= 6:
            result.add(s.lower())
    return result