def find_original_set(*args):
    if len(set(args)) != 35:
        raise ValueError('The function must take exactly 35 distinct arguments.')
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('Each argument must be a set of integers.')
        for element in arg:
            if not isinstance(element, int):
                raise TypeError('Each element in the sets must be an integer.')
        original_set.update(arg)
    return original_set