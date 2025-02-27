def find_original_set(*args):
    if len(args) != 72:
        raise ValueError('Expected exactly 72 sets')
    result_set = set()
    for s in args:
        result_set.update(s)
    return result_set