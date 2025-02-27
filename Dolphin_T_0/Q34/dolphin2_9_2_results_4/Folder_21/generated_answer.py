def find_original_set(*args):
    if len(args) != 851:
        raise ValueError('Exactly 851 distinct arguments are required.')
    result = set()
    for a in args:
        if not isinstance(a, set):
            raise TypeError('Each argument must be a set of integers.')
        result = result.union(a)
    return result