def find_original_set(sets):
    starting_set = sets[0]
    for set in sets[1:]:
        starting_set &= set
    return starting_set