def find_original_set(*args):
    if len(args) != 7:
        raise ValueError('Exactly 7 arguments are required.')
    result = set()
    for s in args:
        result.update(s)
    return result