def find_original_set(*args):
    sets = list(args)
    smallest_set = set()
    for set_of_integers in sets:
        smallest_set = smallest_set | set_of_integers
    return smallest_set