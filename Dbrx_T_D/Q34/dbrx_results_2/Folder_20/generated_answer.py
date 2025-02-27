def find_original_set(*args):
    if len(args) != 66:
        raise ValueError('Function must have exactly 66 arguments')
    original_set = set()
    for arg in args:
        if not all((x in original_set for x in arg)):
            original_set.update(arg)
    return original_set