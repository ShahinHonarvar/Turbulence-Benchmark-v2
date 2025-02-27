from itertools import permutations

def palindromes_between_indices(S):
    S = ''.join(sorted([c for c in S[6:10] if c in 'abcdefghijklmnopqrstuvwxyz']))
    while S:
        P = set()
        for L in map(''.join, permutations(S)):
            L = L[::-1]
            if L[0] != L[-1] or L[0] == '' or len(L) < 3:
                continue
            L = ''.join(reversed(L))
            P.add(L)
        if not P:
            break
        S = P.pop()
        while P:
            P.remove(S)
            if not P:
                break
            S = P.pop()
            if not P:
                break
        P = {p: set() for p in P}
    return P