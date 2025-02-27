def find_original_set(*args):
    result = set()
    for arg in args:
        for elem in arg:
            result.add(elem)
    return result