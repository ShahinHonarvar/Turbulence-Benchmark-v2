def find_original_set(*args):
    if len(args) != 15:
        raise ValueError('Exactly 15 sets must be provided')
    result_set = set()
    for subset in args:
        result_set.update(subset)
    return result_set