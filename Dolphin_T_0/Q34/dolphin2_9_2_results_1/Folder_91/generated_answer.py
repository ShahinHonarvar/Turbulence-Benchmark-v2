def find_original_set(*args):
    result = set()
    for s in args:
        if isinstance(s, set) and len(s) > 0:
            result |= s
    return result