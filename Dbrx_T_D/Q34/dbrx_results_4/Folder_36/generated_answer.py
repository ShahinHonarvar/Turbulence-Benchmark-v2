def find_original_set(*args):
    if len(args) != 714:
        raise ValueError('Function takes exactly 714 arguments')
    if len(args) == 1 and len(args[0]) == 0:
        return set()
    union_set = set()
    for arg in args:
        if not isinstance(arg, set) or len(arg) == 0:
            raise ValueError('Each argument must be a non-empty set')
        union_set.update(arg)
    return union_set