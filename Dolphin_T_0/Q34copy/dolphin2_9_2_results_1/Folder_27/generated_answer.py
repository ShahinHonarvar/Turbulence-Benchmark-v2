def find_original_set(*sets):
    elements = []
    for s in sets:
        for i in s:
            if i not in elements:
                elements.append(i)
    return set(elements)