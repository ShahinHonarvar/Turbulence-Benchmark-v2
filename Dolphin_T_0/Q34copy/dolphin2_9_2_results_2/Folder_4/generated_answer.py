def find_original_set(*args):
    if len(args) != 40:
        raise ValueError('This function needs exactly 40 distinct arguments.')
    result = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('Each argument should be a set of integers.')
        if any((not isinstance(x, int) for x in arg)):
            raise TypeError('Each set should only contain integers.')
        result = result.union(arg)
    return result