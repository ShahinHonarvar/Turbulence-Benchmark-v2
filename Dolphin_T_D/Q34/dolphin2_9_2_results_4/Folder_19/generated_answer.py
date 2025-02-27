def find_original_set(*args):
    result = set()
    for _set in args:
        result |= _set
    return result