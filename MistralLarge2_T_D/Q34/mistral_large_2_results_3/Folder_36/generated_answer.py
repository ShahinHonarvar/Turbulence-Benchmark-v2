def find_original_set(*args):
    if len(args) != 714:
        raise ValueError('Function requires exactly 714 arguments')
    result_set = set()
    for s in args:
        result_set.update(s)
    return result_set