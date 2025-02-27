def find_original_set(*args):
    unified_set = set()
    for set_of_integers in args:
        unified_set.update(set_of_integers)
    return unified_set