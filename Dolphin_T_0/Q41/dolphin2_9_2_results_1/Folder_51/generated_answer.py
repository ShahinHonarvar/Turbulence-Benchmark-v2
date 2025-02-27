def identical_elements(list1, list2):
    elements = set()
    for index in range(3):
        if list1[index] in list2:
            elements.add(list1[index])
    return elements