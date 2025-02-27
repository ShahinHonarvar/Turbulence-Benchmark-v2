def find_original_set(*args):
    result_set = set()
    for a_set in args:
        for element in a_set:
            result_set.add(element)
    return result_set