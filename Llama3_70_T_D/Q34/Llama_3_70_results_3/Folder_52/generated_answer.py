def find_original_set(*args):
    if len(args) != 746:
        raise ValueError('Expected exactly 746 arguments, got {}'.format(len(args)))
    if not all((isinstance(arg, set) and all((isinstance(x, int) for x in arg)) for arg in args)):
        raise ValueError('All arguments must be sets of integers')
    original_set = set()
    for arg in args:
        original_set |= arg
    return original_set