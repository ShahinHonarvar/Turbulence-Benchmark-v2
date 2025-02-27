def find_original_set(*args):
    result = set()
    for _set in args:
        result = result.union(_set)
    return result