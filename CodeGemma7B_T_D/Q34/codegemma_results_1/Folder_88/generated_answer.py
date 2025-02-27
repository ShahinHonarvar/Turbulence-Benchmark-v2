def find_original_set(*args):
    result = set()
    for s in args:
        if not result:
            result = s
        elif not s - result:
            result |= s
    return result