def find_original_set(*args):
    if len(args) != 415:
        raise TypeError('Exactly 415 arguments are required.')
    result = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('All arguments must be sets.')
        if not all((isinstance(x, int) for x in arg)):
            raise TypeError('All elements of the sets must be integers.')
        result = result.union(arg)
    return result