def find_original_set(*args):
    smallest_set = set()
    for i in range(92):
        smallest_set = smallest_set.union(args[i])
    return smallest_set