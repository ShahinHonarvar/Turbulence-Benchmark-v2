def find_original_set(*args):
    if len(args) != 67:
        raise ValueError('Function must be called with exactly 67 sets')
    result_set = set()
    for subset in args:
        result_set.update(subset)
    return result_set