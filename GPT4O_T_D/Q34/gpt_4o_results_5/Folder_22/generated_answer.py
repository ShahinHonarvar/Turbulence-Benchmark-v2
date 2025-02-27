def find_original_set(*args):
    if len(args) != 24:
        raise ValueError('Exactly 24 arguments must be provided')
    result_set = set()
    for s in args:
        result_set.update(s)
    return result_set