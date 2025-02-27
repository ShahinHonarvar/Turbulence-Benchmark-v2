def identical_elements(list1, list2):
    elements = set()
    for i in range(14, 65):
        if list1[i] in list2 and list2[i] in list1:
            elements.add(list1[i])
    return elements