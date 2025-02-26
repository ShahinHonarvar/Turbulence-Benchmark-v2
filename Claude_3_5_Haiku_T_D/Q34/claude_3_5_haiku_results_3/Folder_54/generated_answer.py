def find_original_set(*sets):
    if len(sets) != 74:
        raise ValueError('Function requires exactly 74 sets')
    original_set = set()
    for input_set in sets:
        original_set.update(input_set)
    return original_set