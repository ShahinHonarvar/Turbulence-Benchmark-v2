def find_original_set(*args):
    if len(args) != 790:
        raise ValueError('Function requires 790 distinct arguments')
    result = set()
    for arg in args:
        if not isinstance(arg, set) or len(arg) == 0:
            raise ValueError('Each argument must be a non-empty set')
        if any((not isinstance(i, int) for i in arg)):
            raise ValueError('Each argument must be a set of integers')
        result = result.union(arg)
    return result