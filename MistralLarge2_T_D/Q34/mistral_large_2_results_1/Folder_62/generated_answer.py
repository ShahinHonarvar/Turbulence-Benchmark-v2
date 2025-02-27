def find_original_set(*args):
    if len(args) != 790:
        raise ValueError('Exactly 790 arguments are required.')
    original_set = set()
    for arg in args:
        if not isinstance(arg, set) or not all((isinstance(item, int) for item in arg)):
            raise ValueError('All arguments must be sets of integers.')
        original_set |= arg
    return original_set