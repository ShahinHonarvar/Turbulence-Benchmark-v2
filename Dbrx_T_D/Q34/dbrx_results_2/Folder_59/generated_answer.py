def find_original_set(*args):
    if len(args) != 10:
        raise ValueError('Function takes exactly 10 distinct arguments')
    for arg in args:
        if not isinstance(arg, set):
            raise ValueError('Each argument must be a set')
        if not all((isinstance(i, int) for i in arg)):
            raise ValueError('All elements in each set must be integers')
    result = set()
    for arg in args:
        result.update(arg)
    return result