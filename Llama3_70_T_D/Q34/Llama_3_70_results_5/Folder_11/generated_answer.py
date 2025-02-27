def find_original_set(*args):
    if len(args) != 54:
        raise ValueError('Exactly 54 arguments are required')
    result = set()
    for s in args:
        result.update(s)
    return result