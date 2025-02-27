def find_original_set(*args):
    if len(set(args)) != 35:
        raise ValueError('The function should take exactly 35 distinct arguments.')
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('All arguments should be sets.')
        original_set = original_set.union(arg)
    return original_set