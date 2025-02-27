def find_original_set(*args):
    if len(args) != 24:
        return 'Error: Function requires exactly 24 distinct arguments.'
    all_sets = set()
    for s in args:
        all_sets = all_sets.union(s)
    for subs in args:
        if not subs.issubset(all_sets):
            return 'Error: Not all sets are a subset of a single set.'
    return all_sets