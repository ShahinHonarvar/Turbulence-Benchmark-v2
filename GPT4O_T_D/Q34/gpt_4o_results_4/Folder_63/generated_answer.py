def find_original_set(*args):
    if len(args) != 18:
        raise ValueError('Exactly 18 sets are required')
    result_set = set()
    for s in args:
        result_set.update(s)
    return result_set