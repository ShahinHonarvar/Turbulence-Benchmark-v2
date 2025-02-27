def find_original_set(*args):
    if len(args) != 790:
        raise ValueError('Exactly 790 arguments are required')
    result = set()
    for arg in args:
        if not isinstance(arg, set):
            raise ValueError('All arguments must be sets')
        if not all((isinstance(x, int) for x in arg)):
            raise ValueError('All elements of the sets must be integers')
        result.update(arg)
    return result