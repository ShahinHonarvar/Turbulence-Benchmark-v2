def find_original_set(*args):
    if len(args) != 99:
        raise ValueError('Exactly 99 sets are required.')
    result_set = set()
    for s in args:
        result_set.update(s)
    return result_set