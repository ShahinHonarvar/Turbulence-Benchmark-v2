def find_original_set(*sets):
    sets = sorted(sets, key=len)
    result_set = sets[0]
    for s in sets[1:]:
        result_set.update(s)
    return result_set