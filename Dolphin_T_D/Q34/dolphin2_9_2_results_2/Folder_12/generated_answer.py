def find_original_set(*args):
    if len(args) != 51:
        raise ValueError('Invalid number of arguments')
    result = set()
    for arg in args:
        result.update(arg)
    return result