def find_original_set(*args):
    if len(args) != 459:
        raise ValueError('The function should take exactly 459 arguments.')
    min_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('All arguments must be sets.')
        min_set.update(arg)
    return min_set