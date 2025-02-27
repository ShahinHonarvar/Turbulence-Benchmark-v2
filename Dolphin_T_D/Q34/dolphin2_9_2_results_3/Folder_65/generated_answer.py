def find_original_set(*args):
    result_set = set()
    for set in args:
        for num in set:
            result_set.add(num)
    return result_set