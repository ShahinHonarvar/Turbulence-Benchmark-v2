def find_original_set(*args):
    if len(args) != 80:
        raise ValueError('Exactly 80 sets are required')
    original_set = set()
    for s in args:
        original_set.update(s)
    return original_set