def find_original_set(*args):
    if len(args) != 90:
        raise ValueError('Exactly 90 arguments are required')
    result = set()
    for arg in args:
        result.update(arg)
    return result