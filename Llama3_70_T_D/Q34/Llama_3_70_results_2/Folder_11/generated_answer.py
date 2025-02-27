def find_original_set(*args):
    if len(args) != 54:
        raise ValueError('Exactly 54 arguments are required')
    if not all((isinstance(arg, set) for arg in args)):
        raise ValueError('All arguments must be sets')
    if not all((all((isinstance(i, int) for i in arg)) for arg in args)):
        raise ValueError('All elements of the sets must be integers')
    result = set()
    for arg in args:
        result = result.union(arg)
    return result