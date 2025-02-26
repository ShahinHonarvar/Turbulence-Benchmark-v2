def find_original_set(*args):
    if len(args) != 97:
        raise ValueError('Function requires exactly 97 distinct arguments')
    original_set = set()
    for subset in args:
        original_set.update(subset)
    return original_set