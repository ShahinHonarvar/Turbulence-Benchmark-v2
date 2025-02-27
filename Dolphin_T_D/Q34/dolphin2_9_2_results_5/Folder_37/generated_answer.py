def find_original_set(*args):
    sets = list(args)
    smallest_set = set()
    while sets:
        smallest_set = smallest_set.union(sets.pop(0))
        for s in sets[:]:
            if s.contained_by(smallest_set):
                sets.remove(s)
    return smallest_set