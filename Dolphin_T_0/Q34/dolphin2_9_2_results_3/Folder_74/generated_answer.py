def find_original_set(*args):
    smallest_set = args[0]
    for i in range(1, 96):
        smallest_set = smallest_set.union(args[i])
    return smallest_set