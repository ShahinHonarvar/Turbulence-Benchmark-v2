def find_original_set(*args):
    if len(args) != 90:
        raise ValueError('Exactly 90 arguments are required')
    if not all((isinstance(arg, set) and all((isinstance(i, int) for i in arg)) for arg in args)):
        raise ValueError('All arguments must be sets of integers')
    return {i for arg in args for i in arg}