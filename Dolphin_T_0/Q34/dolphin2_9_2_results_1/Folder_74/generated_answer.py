def find_original_set(*args):
    if len(args) != 96:
        return 'Invalid number of arguments. Expected 96 distinct sets of integers.'
    sets = [set(arg) for arg in args]
    original_set = sets[0]
    for i in range(1, len(sets)):
        original_set = original_set.union(sets[i])
    return original_set