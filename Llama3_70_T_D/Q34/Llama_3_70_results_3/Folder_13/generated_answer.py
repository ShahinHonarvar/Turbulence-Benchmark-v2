def find_original_set(*args):
    if len(args) != 845:
        raise TypeError('find_original_set() takes exactly 845 arguments')
    original_set = set()
    for arg in args:
        if not isinstance(arg, set) or not arg.issubset([x for x in arg if isinstance(x, int)]):
            raise TypeError('All arguments must be sets of integers')
        original_set = original_set.union(arg)
    return original_set