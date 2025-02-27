from itertools import permutations

def palindromes_between_indices(s):
    p = []
    a = s[5:9]
    for i in permutations(a):
        if i[0] in string.ascii_uppercase:
            p.append(''.join(i).upper())
        else:
            p.append(''.join(i))
    return set(p)