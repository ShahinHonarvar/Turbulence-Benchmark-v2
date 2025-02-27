def find_original_set(*args):
    if len(args) != 990:
        raise ValueError('Exactly 990 distinct arguments must be passed to the function')
    s = set()
    for a in args:
        if not isinstance(a, set):
            raise TypeError('All arguments must be sets of integers')
        if not a.issubset(s):
            s |= a
    return s