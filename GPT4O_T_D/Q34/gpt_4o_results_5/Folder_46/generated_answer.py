def find_original_set(*args):
    if len(args) != 828:
        raise ValueError('The function requires exactly 828 arguments.')
    result_set = set()
    for s in args:
        result_set.update(s)
    return result_set