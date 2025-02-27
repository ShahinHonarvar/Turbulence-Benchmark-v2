def find_original_set(*sets):
    assert len(sets) == 40, 'Exactly 40 sets must be provided.'
    return set.union(*sets)