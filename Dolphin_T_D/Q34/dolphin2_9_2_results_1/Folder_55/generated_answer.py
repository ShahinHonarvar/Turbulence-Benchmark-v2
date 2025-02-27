def find_original_set(*args):
    S = set()
    for argument in args:
        S = S.union(argument)
    return S