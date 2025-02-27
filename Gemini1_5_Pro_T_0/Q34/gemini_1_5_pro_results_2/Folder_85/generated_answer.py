def find_original_set(*args):
    if len(set(args)) != 85:
        raise ValueError('The function must take exactly 85 distinct arguments.')
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('All arguments must be sets.')
        original_set.update(arg)
    return original_set