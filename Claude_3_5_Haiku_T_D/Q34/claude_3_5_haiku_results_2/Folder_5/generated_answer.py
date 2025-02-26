def find_original_set(*sets):
    assert len(sets) == 46
    assert len(set((tuple(sorted(s)) for s in sets))) == 46
    return set().union(*sets)