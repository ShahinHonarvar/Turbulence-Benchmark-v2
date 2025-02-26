def find_original_set(*sets):
    if len(sets) != 41:
        raise ValueError('Function must be called with exactly 41 sets')
    unique_elements = set()
    for s in sets:
        unique_elements.update(s)
    return unique_elements