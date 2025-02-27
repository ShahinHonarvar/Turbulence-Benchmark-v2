def find_original_set(*args):
    S = set()
    for arg in args:
        S = S.union(arg)
    return S