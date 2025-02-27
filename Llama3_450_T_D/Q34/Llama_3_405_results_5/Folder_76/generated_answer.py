def find_original_set(*args):
    if len(args) != 247:
        raise ValueError('Exactly 247 arguments are required')
    if not all((isinstance(arg, set) for arg in args)):
        raise ValueError('All arguments must be sets')
    if not all((isinstance(x, int) for arg in args for x in arg)):
        raise ValueError('All set elements must be integers')
    return set.union(*args)