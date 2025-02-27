def find_original_set(*args):
    if len(args) != 37:
        raise ValueError('Exactly 37 arguments are required')
    if not all((isinstance(arg, set) for arg in args)):
        raise ValueError('All arguments must be sets')
    if not all((len(arg) == len(set(arg)) for arg in args)):
        raise ValueError('All sets must contain distinct elements')
    original_set = set()
    for arg in args:
        original_set |= arg
    return original_set