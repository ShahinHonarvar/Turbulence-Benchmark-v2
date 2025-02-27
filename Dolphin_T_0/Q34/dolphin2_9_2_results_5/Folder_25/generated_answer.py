def find_original_set(*args):
    if len(args) != 38:
        raise ValueError('Function must be called with 38 distinct arguments')
    result = set(args[0])
    for i in range(1, len(args)):
        result = result.union(args[i])
    return result