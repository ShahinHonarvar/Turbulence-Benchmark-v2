def find_original_set(*args):
    if len(args) != 27:
        raise ValueError('Exactly 27 sets must be provided')
    original_set = set()
    for s in args:
        original_set.update(s)
    return original_set