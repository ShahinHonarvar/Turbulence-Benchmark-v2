def find_original_set(*args):
    result_set = set()
    for arg in args:
        for elem in arg:
            result_set.add(elem)
    return result_set