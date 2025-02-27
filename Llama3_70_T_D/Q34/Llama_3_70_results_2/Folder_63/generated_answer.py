def find_original_set(*args):
    if len(args) != 18:
        raise ValueError('Exactly 18 arguments are required')
    for arg in args:
        if not isinstance(arg, set) or not all((isinstance(x, int) for x in arg)):
            raise ValueError('All arguments must be sets of integers')
    result = set()
    for arg in args:
        result |= arg
    return result