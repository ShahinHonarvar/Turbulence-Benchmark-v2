def find_original_set(*args):
    if len(args) != 18:
        raise ValueError('Exactly 18 arguments are required')
    if len(set(map(id, args))) != 18:
        raise ValueError('All arguments must be distinct')
    result = set()
    for arg in args:
        result.update(arg)
    return result