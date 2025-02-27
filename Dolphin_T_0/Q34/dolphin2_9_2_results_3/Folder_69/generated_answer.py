def find_original_set(*args):
    result = set()
    for arg in args:
        for element in arg:
            result.add(element)
    return result