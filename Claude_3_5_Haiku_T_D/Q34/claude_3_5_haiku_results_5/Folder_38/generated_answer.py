def find_original_set(*sets):
    unique_elements = set()
    for s in sets:
        unique_elements.update(s)
    return unique_elements