def find_original_set(*args):
    result_set = set()
    for a_set in args:
        result_set |= a_set
    return result_set