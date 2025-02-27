def find_original_set(*sets):
    sets = set(sets)
    while any((s - sets.union(*sets - {s}) for s in sets)):
        sets.remove(max(sets, key=lambda s: len(s - sets.union(*sets - {s}))))
    return sets.union(*sets)