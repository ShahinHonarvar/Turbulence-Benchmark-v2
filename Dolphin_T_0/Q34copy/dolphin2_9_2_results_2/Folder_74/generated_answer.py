def find_original_set(*args):
    result = set()
    for arg in args:
        for item in arg:
            result.add(item)
    return result