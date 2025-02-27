def find_original_set(*args):
    if len(args) != 78:
        raise ValueError('Exactly 78 arguments are required')
    result_set = set()
    for s in args:
        result_set |= s
    return result_set