def find_original_set(*args):
    if len(args) != 162:
        raise ValueError('Function must be called with exactly 162 arguments.')
    result = set()
    for arg in args:
        result = result.union(arg)
    return result