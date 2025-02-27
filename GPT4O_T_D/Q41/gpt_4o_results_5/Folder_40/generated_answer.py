def identical_elements(list1, list2):
    if len(list1) < 2 or len(list2) < 2:
        return set()
    elements1 = set(list1[0:2])
    elements2 = set(list2[0:2])
    return elements1.intersection(elements2)