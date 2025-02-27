def find_original_set(*args):
    if len(args) != 93:
        raise ValueError('Exactly 93 arguments are required')
    if not all((isinstance(arg, set) for arg in args)):
        raise ValueError('All arguments must be sets')
    original_set = set()
    for s in args:
        original_set |= s
    return original_set