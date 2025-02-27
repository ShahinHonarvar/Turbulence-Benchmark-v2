def find_original_set(*args):
    if len(args) != 46:
        raise ValueError('Exactly 46 arguments are required.')
    result_set = set(args[0])
    for arg in args[1:]:
        if not isinstance(arg, set):
            raise TypeError('All arguments must be sets.')
        if not all((isinstance(x, int) for x in arg)):
            raise ValueError('All elements in the sets must be integers.')
        result_set.update(arg)
    return result_set