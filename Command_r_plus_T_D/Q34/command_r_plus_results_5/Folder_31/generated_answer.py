def find_original_set(*args):
    if len(args) != 34:
        raise ValueError('Exactly 34 arguments are required.')
    if len(args) != len(set(args)):
        raise ValueError('Arguments must be distinct.')
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set