def find_original_set(*args):
    if len(args) != 126:
        raise ValueError('Function must take exactly 126 distinct arguments')
    for arg in args:
        if not isinstance(arg, set) or not all((isinstance(i, int) for i in arg)):
            raise ValueError('All arguments must be sets of integers')
        if len(arg) != len(set(arg)):
            raise ValueError('All arguments must be sets of distinct integers')
    return set.union(*args)