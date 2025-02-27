def find_original_set(*sets):
    elements = set()
    for s in sets:
        elements.update(s)
    return elements