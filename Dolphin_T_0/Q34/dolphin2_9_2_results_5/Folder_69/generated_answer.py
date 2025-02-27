def find_original_set(*args):
    result = set()
    for arg in args:
        if isinstance(arg, set) and len(arg) > 0:
            result.update(arg)
    return result