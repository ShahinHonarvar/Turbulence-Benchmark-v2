from itertools import combinations

def palindromes_between_indices(s):
    res = set()
    sub = ''.join(sorted((ch for ch in s[1:7] if ch.isalpha() and ch.isascii())))
    if len(sub) < 3:
        return res
    for i in range(3, len(sub) + 1):
        for combo in combinations(sub, i):
            for word in ''.join(combo).lower():
                rev = word[::-1]
                res.add(word)
                if word != rev and rev[len(word) // 2] not in res:
                    continue
                if rev.find(word) != -1 and rev != word:
                    res.add(rev)
    return res