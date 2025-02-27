def find_original_set(*args):
    result = {}
    for arg in args:
        for e in arg:
            result.add(e)
    return result