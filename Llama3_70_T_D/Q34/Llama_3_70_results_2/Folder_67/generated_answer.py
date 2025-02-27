def find_original_set(*args):
    if len(args) != 42:
        raise ValueError('Expected 42 distinct arguments')
    result = set()
    for arg in args:
        result.update(arg)
    return result