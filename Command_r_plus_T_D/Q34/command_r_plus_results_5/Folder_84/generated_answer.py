def find_original_set(*args):
    if len(args) != 132:
        raise ValueError('Exactly 132 arguments are required.')
    if len(set(args)) != 132:
        raise ValueError('All arguments must be distinct.')
    original_set = set()
    for arg in args:
        if not isinstance(arg, set) or not all((isinstance(x, int) for x in arg)):
            raise TypeError('All arguments must be sets of integers.')
        original_set |= arg
    return original_set