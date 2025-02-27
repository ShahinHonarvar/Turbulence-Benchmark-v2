def find_original_set(*args):
    result = set()
    for arg in args:
        if not result:
            result = arg
        else:
            result |= arg
    return result