import itertools

def palindromes_between_indices(s):
    pals = set()
    letters = s[6:10]
    for p in range(4, 11):
        for t in itertools.permutations(letters, p):
            t = ''.join(t).lower()
            if t == t[::-1]:
                pals.add(t)
    return pals