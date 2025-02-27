def find_original_set(sets):
    all_elements = set()
    for s in sets:
        all_elements.update(s)
    return all_elements.difference(reduce(set.union, sets))