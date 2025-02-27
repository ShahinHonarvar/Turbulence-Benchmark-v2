def find_original_set(*args):
    if len(args) != 47:
        raise ValueError('Exactly 47 arguments are expected')
    result_set = set()
    for s in args:
        result_set |= s
    return result_set