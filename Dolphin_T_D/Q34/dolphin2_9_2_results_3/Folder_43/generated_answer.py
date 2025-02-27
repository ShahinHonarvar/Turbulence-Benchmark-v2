def find_original_set(*args):
    S = set()
    for s in args:
        S = S.union(s)
    return S