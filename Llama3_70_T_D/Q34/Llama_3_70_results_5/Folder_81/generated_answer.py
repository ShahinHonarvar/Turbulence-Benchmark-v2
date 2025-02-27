def find_original_set(*args):
    if len(args) != 72:
        raise TypeError('Exactly 72 arguments are required')
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set