def find_original_set(*args):
    if len(args) != 41:
        raise ValueError('Exactly 41 distinct arguments are required.')
    original_set = set()
    for subset in args:
        original_set.update(subset)
    return original_set