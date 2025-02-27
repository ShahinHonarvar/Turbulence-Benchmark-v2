def find_original_set(*args):
    if len(args) != 59:
        raise ValueError('The function takes exactly 59 distinct arguments')
    set_union = set()
    for s in args:
        if not isinstance(s, set) or not s.issubset(set_union):
            raise ValueError('Each argument must be a set of integers')
        set_union = set_union.union(s)
    return set_union