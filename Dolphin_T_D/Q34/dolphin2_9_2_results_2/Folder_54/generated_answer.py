def find_original_set(*args):
    result_set = set()
    for set_of_integers in args:
        result_set = result_set.union(set_of_integers)
    return result_set