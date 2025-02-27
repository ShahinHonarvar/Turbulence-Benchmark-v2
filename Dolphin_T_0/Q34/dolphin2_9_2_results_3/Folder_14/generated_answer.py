def find_original_set(*args):
    if len(args) != 13:
        return 'The function requires exactly 13 distinct sets of integers as arguments.'
    sets = [set(s) for s in args]
    original_set = sets[0]
    for s in sets[1:]:
        original_set = original_set.union(s)
    return original_set