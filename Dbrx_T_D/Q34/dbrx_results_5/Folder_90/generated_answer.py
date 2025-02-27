def find_original_set(sets):
    total_elements = set()
    for s in sets:
        for element in s:
            total_elements.add(element)
    return total_elements