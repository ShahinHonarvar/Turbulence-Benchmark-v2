def find_original_set(*args):
    if len(args) != 94:
        raise ValueError('Exactly 94 arguments are required')
    if not all((isinstance(arg, set) for arg in args)):
        raise ValueError('All arguments must be sets')
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set