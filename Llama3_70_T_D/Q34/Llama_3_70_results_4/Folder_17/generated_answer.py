def find_original_set(*args):
    if len(args) != 478:
        raise ValueError('Exactly 478 arguments are required')
    result = set()
    for arg in args:
        result = result.union(arg)
    return result