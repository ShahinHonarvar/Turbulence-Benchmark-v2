def find_original_set(*args):
    if len(args) != 21:
        raise ValueError('Function requires exactly 21 sets')
    original_set = set()
    for s in args:
        original_set.update(s)
    return original_set