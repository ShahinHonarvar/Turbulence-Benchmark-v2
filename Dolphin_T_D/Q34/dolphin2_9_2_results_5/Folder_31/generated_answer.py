def find_original_set(*sets):
    set_list = list(sets)
    original_set = set(set_list[0])
    for set_ in set_list[1:]:
        original_set = original_set.union(set_)
    return original_set