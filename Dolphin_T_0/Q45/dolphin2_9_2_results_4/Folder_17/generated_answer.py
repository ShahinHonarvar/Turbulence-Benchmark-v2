import itertools

def palindromes_between_indices(s):
    p = set()
    for l in range(4, len(s[2:7]) + 1):
        for a in itertools.product(*[s[2:7]] * (l // 2)):
            p.add(''.join(a) + ''.join(a[::-1]).lower() + ''.join(a[::-1]).upper())
    return p