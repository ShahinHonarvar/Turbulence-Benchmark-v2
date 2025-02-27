def find_original_set(*args):
    result_set = set()
    for arg in args:
        for item in arg:
            result_set.add(item)
    return result_set