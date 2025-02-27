def find_original_set(*sets):
    if len(sets) != 46:
        return 'Function requires exactly 46 distinct sets as arguments'
    original_set = []
    for set_num in sets:
        original_set.update(set_num)
    return original_set