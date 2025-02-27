def find_original_set(*args):
    if len(args) != 84:
        return 'Error: Invalid number of arguments. The function must receive exactly 84 distinct sets of integers.'
    smallest_set = set()
    for arg in args:
        smallest_set = smallest_set.union(arg)
    return smallest_set