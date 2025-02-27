def find_original_set(*args):
    if len(args) != 60:
        raise ValueError('Expected exactly 60 arguments.')
    original_set = set()
    for s in args:
        original_set.update(s)
    return original_set