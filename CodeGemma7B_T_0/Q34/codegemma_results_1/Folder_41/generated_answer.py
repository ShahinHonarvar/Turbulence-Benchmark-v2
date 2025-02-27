def find_original_set(*sets):
    if len(sets) != 20:
        raise ValueError('The function should take exactly 20 distinct arguments')
    min_set = set()
    for s in sets:
        if not s.issubset(min_set):
            min_set = s
    return min_set