def find_original_set(*args):
    result_set = set()
    for arg in args:
        for num in arg:
            result_set.add(num)
    return result_set