def find_original_set(sets):
    sets_set = set.intersection(*sets)
    return set(range(min(sets_set), max(sets_set) + 1))