def find_original_set(*args):
    result = set()
    for each_set in args:
        result |= each_set
    return result