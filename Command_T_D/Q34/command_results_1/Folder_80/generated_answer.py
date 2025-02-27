from itertools import combinations

def find_original_set(X):
    S = set(X[0])
    for x in X[1:]:
        S.update(x)
    for e in S:
        if not all((e in x for x in X)):
            S.remove(e)
    return S