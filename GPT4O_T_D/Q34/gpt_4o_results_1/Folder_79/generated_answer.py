def find_original_set(*args):
    if len(args) != 17:
        raise ValueError('Exactly 17 sets must be provided')
    original_set = set()
    for subset in args:
        original_set = original_set.union(subset)
    return original_set