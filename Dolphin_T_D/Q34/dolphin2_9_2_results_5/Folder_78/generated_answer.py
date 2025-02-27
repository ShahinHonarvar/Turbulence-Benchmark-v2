def find_original_set(*args):
    result = set()
    for arg in args:
        result |= set(arg)
    return result