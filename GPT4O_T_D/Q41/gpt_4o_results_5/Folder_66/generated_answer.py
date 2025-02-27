def identical_elements(list1, list2):
    elements1 = set(list1[50:55])
    elements2 = set(list2[50:55])
    return elements1.intersection(elements2)