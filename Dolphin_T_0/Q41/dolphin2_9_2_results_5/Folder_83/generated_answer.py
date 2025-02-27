def identical_elements(list1, list2):
    elements = set()
    for i in range(90, 201):
        if (i < len(list1) and i < len(list2)) and (list1[i] in list2 and list1[i] not in elements):
            elements.add(list1[i])
    return elements