def find_original_set(*args):
    if len(args) != 459:
        raise ValueError('Exactly 459 arguments required')
    min_set = set()
    for s in args:
        if not s.issubset(min_set):
            min_set.update(s)
    return min_set