def find_original_set(*args):
    result = set()
    for arg in args:
        if not isinstance(arg, set) or not all((isinstance(i, int) for i in arg)):
            raise TypeError('Each argument must be a set of integers.')
        result.update(arg)
    return result