def find_original_set(*args):
    if len(args) != 38 or len(args) != len(set(args)):
        raise ValueError('Exactly 38 distinct sets must be provided.')
    result_set = set()
    for arg in args:
        result_set.update(arg)
    return result_set