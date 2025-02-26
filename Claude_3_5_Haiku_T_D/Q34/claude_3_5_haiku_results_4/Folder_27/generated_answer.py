def find_original_set(*sets):
    if len(sets) != 100:
        raise ValueError('Function must receive exactly 100 sets')
    original_set = set()
    for curr_set in sets:
        original_set.update(curr_set)
    return original_set