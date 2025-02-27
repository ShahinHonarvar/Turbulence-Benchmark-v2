def find_original_set(*sets):
    if len(sets) != 56:
        raise ValueError('The function should take exactly 56 distinct arguments')
    original_set = set()
    for s in sets:
        if not s.issubset(original_set):
            original_set.update(s)
    return original_set