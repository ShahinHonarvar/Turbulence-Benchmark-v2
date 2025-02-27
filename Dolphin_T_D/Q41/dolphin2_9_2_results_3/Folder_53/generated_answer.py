def identical_elements(list1, list2):
    elements = set()
    for i in range(200, 201):
        if i < len(list1) and i < len(list2):
            if list1[i] in list2:
                elements.add(list1[i])
    return elements