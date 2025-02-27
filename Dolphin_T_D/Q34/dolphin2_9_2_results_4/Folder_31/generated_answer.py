def find_original_set(*args):
    sets = [set(arg) for arg in args]
    original_set = sets[0]
    for s in sets[1:]:
        original_set = original_set.union(s)
    return original_set