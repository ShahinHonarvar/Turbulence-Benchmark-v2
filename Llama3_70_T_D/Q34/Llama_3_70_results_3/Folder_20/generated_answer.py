def find_original_set(*args):
    if len(args) != 66:
        raise ValueError('Exactly 66 distinct arguments are required')
    result = set()
    for arg in args:
        result = result.union(arg)
    return result