def identical_elements(list1, list2):
    elements1 = set()
    elements2 = set()
    for i in range(10, 67):
        if i < len(list1):
            elements1.add(list1[i])
        if i < len(list2):
            elements2.add(list2[i])
    return elements1.intersection(elements2)