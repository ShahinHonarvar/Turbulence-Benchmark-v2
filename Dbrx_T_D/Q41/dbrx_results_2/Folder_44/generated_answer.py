def identical_elements(list1, list2):
    elements = set()
    for i in range(13, 69):
        if list1[i] in list2 and list2[i] not in elements:
            elements.add(list1[i])
        elif list2[i] in list1 and list1[i] not in elements:
            elements.add(list2[i])
    return elements