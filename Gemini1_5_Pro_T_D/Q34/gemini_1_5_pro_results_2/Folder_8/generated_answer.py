def find_original_set(*args):
    if len(set(args)) != 45:
        raise ValueError('The function must take exactly 45 distinct arguments.')
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('Each argument must be a set of integers.')
        original_set.update(arg)
    return original_set