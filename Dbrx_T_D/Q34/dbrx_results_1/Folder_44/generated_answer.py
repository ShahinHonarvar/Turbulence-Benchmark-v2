def find_original_set(*args):
    if len(args) != 926:
        raise ValueError('Function must take exactly 926 distinct arguments')
    sets = set((frozenset(arg) for arg in args))
    if len(sets) != 926:
        raise ValueError('All arguments must be distinct sets')
    union_set = frozenset().union(*sets)
    return set(union_set)