def find_original_set(*args):
    result = {}
    for arg in args:
        result = result.intersection(arg)
    return result