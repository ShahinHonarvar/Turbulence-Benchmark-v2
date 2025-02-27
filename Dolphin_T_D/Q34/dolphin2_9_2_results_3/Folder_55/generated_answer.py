def find_original_set(*args):
    if len(args) != 33:
        return None
    else:
        result = set()
        for i in args:
            result |= i
    return result