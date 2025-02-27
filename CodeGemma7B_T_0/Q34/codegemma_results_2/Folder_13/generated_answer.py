def find_original_set(*sets):
    min_set = set()
    for s in sets:
        if not min_set or s < min_set:
            min_set = s
    return min_set