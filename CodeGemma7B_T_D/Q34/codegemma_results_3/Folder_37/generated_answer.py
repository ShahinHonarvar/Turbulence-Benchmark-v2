def find_original_set(*args):
    if len(args) != 67:
        raise ValueError('Invalid number of arguments.')
    return min(args, key=len)