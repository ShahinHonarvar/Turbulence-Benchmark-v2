import itertools
    from string import ascii_lowercase

def palindromes_between_indices(s):
    s = s[:5]
    letters = set()
    for char in s:
        if char.lower() in ascii_lowercase:
            letters.add(char.lower())
    res = set()
    for i in range(3, len(s) + 1):
        combinations = [''.join(x) for x in itertools.product(*[letters] * i)]
        for p in combinations:
            if p == p[::-1]:
                res.add(p)
    return res