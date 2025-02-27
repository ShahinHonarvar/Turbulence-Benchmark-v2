def find_original_set(*args):
    if len(args) != 91:
        raise ValueError('The function requires exactly 91 arguments')
    result_set = set()
    for s in args:
        result_set = result_set.union(s)
    return result_set