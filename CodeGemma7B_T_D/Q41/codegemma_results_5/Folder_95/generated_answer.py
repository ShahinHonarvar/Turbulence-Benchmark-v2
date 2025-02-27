def identical_elements(list1, list2):
    elements = set()
    for i in range(82, 87):
        if list1[i] in list2[i]:
            elements.add(list1[i])
    return elements or set()