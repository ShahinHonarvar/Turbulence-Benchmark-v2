def find_original_set(*args):
    if len(args) != 132:
        raise ValueError('Function requires exactly 132 arguments')
    original_set = set()
    for s in args:
        original_set.update(s)
    return original_set