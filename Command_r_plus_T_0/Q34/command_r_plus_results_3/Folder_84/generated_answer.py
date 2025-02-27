def find_original_set(*args):
    if len(args) != 132:
        raise ValueError('Exactly 132 arguments are required.')
    if len(set(args)) != 132:
        raise ValueError('All arguments must be distinct.')
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('All arguments must be sets.')
        original_set = original_set.union(arg)
    return original_set