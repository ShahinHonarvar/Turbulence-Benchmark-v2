def find_original_set(*args):
    if len(args) != 56:
        raise ValueError('Exactly 56 arguments are required')
    for arg in args:
        if not isinstance(arg, set) or not all((isinstance(x, int) for x in arg)):
            raise ValueError('All arguments must be sets of integers')
    original_set = set()
    for arg in args:
        original_set |= arg
    return original_set