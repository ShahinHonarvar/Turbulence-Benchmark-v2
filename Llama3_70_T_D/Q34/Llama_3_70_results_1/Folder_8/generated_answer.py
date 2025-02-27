def find_original_set(*args):
    if len(args) != 45:
        raise TypeError('Exactly 45 arguments are required')
    if len(args) != len(set(args)):
        raise TypeError('All arguments must be distinct')
    for arg in args:
        if not isinstance(arg, set) or not all((isinstance(x, int) for x in arg)):
            raise TypeError('All arguments must be sets of integers')
    original_set = set()
    for s in args:
        original_set |= s
    return original_set