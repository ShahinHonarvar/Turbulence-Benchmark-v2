def find_original_set(*sets):
    if len(sets) != 15:
        return 'Function requires exactly 15 sets as arguments.'
    original_set = set()
    for s in sets:
        if not isinstance(s, set) or not s.issubset(s):
            return 'All arguments must be subsets of a set of integers.'
        original_set = original_set.union(s)
    return original_set