def find_original_set(*args):
    if len(args) != 100:
        raise ValueError('The function requires exactly 100 arguments.')
    original_set = set()
    for subset in args:
        original_set = original_set.union(subset)
    return original_set