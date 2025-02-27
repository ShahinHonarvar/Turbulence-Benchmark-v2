def find_original_set(*args):
    if len(args) != 27:
        raise ValueError('Exactly 27 arguments are required.')
    if len(args) != len(set(args)):
        raise ValueError('Arguments must be distinct sets.')
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set