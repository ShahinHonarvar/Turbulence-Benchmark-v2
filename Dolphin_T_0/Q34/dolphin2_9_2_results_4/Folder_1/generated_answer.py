def find_original_set(*args):
    result = {}
    for arg in args:
        if isinstance(arg, set):
            result |= arg
    return set(result)