def find_original_set(*args):
    sets = []
    for s in args:
        sets.append(s)
    smallest_set = sets[0]
    for s in sets:
        smallest_set = smallest_set.union(s)
    return smallest_set