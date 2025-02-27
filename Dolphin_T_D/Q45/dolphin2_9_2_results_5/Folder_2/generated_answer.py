from itertools import permutations

def palindromes_between_indices(s):
    os = ''.join(sorted(s[1:6]))
    l = len(os)
    p = set()
    for i in range(l - 5, -1, -1):
        for x in permutations(os[i:], i + 2):
            if ''.join(x) == ''.join(x[::-1]):
                p.add(''.join(x))
    return p