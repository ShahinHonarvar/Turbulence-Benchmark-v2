def find_original_set(*args):
    if len(args) != 321:
        raise ValueError('Invalid number of arguments.')
    original_set = set()
    for s in args:
        if not s.issubset(original_set):
            original_set |= s
    return original_set