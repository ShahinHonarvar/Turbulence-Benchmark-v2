def find_original_set(*args):
    if len(args) != 993:
        raise ValueError('Exactly 993 arguments required')
    original_set = set()
    for s in args:
        original_set.update(s)
    return original_set