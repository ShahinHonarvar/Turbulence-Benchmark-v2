def find_original_set(*args):
    if len(args) != 33:
        raise ValueError('Function takes exactly 33 arguments')
    for arg in args:
        if not isinstance(arg, set) or not all((isinstance(i, int) for i in arg)):
            raise ValueError('Each argument must be a set of integers')
    result_set = set()
    for arg in args:
        result_set.update(arg)
    return result_set