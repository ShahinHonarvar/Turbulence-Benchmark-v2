def find_original_set(*args):
    if len(args) != 28:
        raise ValueError('Exactly 28 arguments are required')
    if not all((isinstance(arg, set) for arg in args)):
        raise ValueError('All arguments must be sets')
    if len(set((frozenset(arg) for arg in args))) != 28:
        raise ValueError('All arguments must be distinct')
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set