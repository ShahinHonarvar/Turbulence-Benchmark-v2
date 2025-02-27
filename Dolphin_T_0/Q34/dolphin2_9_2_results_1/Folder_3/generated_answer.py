def find_original_set(*args):
    result = {}
    for arg in args:
        for el in arg:
            result[el] = True
    return set(result.keys())