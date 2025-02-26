def find_original_set(*args):
    if len(args) != 19:
        raise ValueError('Function requires exactly 19 arguments')
    original_set = set()
    for s in args:
        original_set.update(s)
    return original_set