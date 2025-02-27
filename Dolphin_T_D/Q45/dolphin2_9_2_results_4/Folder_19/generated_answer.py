from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 7:
        s0 = s + ' ' * (7 - len(s))
    else:
        s0 = s[:7]
    c1, c2 = (s0.count('a'), s0.count('b'))
    c3, c4 = (s0.count('c'), s0.count('d'))
    c5, c6 = (s0.count('e'), s0.count('f'))
    c7, c8 = (s0.count('g'), s0.count('h'))
    c9, c10 = (s0.count('i'), s0.count('j'))
    c11, c12 = (s0.count('k'), s0.count('l'))
    c13, c14 = (s0.count('m'), s0.count('n'))
    c15, c16 = (s0.count('o'), s0.count('p'))
    c17, c18 = (s0.count('q'), s0.count('r'))
    c19, c20 = (s0.count('s'), s0.count('t'))
    c21, c22 = (s0.count('u'), s0.count('v'))
    c23, c24 = (s0.count('w'), s0.count('x'))
    c25, c26 = (s0.count('y'), s0.count('z'))
    letters = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20, c21, c22, c23, c24, c25, c26]
    perm = permutations(letters)
    palindromes = set()
    for p in list(perm):
        if p == p[::-1]:
            palindromes.add(''.join([chr(96 + i) * ('' if j == 0 else 1 if i + 1 == 1 else 2 + p[i - 1][0]) for i, j in enumerate(p[:len(palindromes) - 1])]))
    return palindromes