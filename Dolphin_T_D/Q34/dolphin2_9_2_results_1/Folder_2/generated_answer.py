def find_original_set(*args):
    result = set()
    for arg in args:
        if isinstance(arg, set):
            result = result | arg
    return result