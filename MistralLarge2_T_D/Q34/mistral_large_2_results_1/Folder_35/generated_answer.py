def find_original_set(*sets):
    if len(sets) != 702:
        raise ValueError('Exactly 702 arguments are required.')
    all_elements = set()
    for s in sets:
        all_elements.update(s)
    return all_elements