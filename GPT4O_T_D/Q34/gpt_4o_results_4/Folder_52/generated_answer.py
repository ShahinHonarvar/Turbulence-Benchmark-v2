def find_original_set(*args):
    if len(args) != 746:
        raise ValueError('Expected exactly 746 arguments')
    result_set = set()
    for s in args:
        result_set.update(s)
    return result_set