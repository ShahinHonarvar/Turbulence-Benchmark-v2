def find_original_set(*sets):
    if len(sets) != 72:
        raise ValueError('Function must receive exactly 72 sets')
    unique_elements = set()
    for s in sets:
        unique_elements.update(s)
    return unique_elements