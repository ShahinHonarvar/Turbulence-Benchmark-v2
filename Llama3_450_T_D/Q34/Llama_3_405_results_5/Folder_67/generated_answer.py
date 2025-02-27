def find_original_set(*args):
    if len(args) != 42:
        raise TypeError('Expected exactly 42 arguments')
    for arg in args:
        if not isinstance(arg, set) or not all((isinstance(x, int) for x in arg)):
            raise TypeError('All arguments must be sets of integers')
    original_set = set()
    for arg in args:
        original_set |= arg
    return original_set