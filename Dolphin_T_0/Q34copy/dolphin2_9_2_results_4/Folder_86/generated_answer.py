def find_original_set(*sets):
    list_sets = list(sets)
    smallest_set = list_sets[0]
    for current_set in list_sets[1:]:
        for integer in current_set:
            if integer not in smallest_set:
                smallest_set.add(integer)
    return smallest_set