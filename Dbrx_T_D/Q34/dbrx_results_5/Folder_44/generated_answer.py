def find_original_set(*args):
    if len(args) != 926:
        raise ValueError('Function takes exactly 926 arguments')
    result_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise ValueError('Each argument must be a set')
        if not all((isinstance(i, int) for i in arg)):
            raise ValueError('All elements in the sets must be integers')
        result_set.update(arg)
    return result_set