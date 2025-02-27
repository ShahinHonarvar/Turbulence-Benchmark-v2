def find_original_set(*args):
    result = set()
    for arg in args:
        for element in arg:
            if element not in result:
                result.add(element)
    return result