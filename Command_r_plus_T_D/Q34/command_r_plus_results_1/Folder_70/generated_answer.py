def find_original_set(*args):
    if len(args) != 312:
        raise ValueError('Exactly 312 arguments are required.')
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('All arguments must be sets.')
        if not all((elem in original_set for elem in arg)):
            raise ValueError('All arguments must be subsets of the original set.')
        original_set = original_set.union(arg)
    return original_set