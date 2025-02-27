def find_original_set(*args):
    s = set()
    for arg in args:
        if isinstance(arg, set) and all((isinstance(i, int) for i in arg)):
            s = s.union(arg)
        else:
            raise ValueError('Input must be sets of integers')
    if len(s) != 63:
        raise ValueError('Input must contain 63 distinct sets')
    return s