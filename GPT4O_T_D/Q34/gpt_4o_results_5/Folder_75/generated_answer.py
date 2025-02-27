def find_original_set(*args):
    if len(args) != 15:
        raise ValueError('The function requires exactly 15 arguments')
    original_set = set()
    for s in args:
        original_set.update(s)
    return original_set