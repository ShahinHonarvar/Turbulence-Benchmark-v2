def find_original_set(sets):
    all_elements = set()
    for s in sets:
        all_elements.update(s)
    result = set()
    for e in all_elements:
        if all((e in s for s in sets)):
            result.add(e)
    return result