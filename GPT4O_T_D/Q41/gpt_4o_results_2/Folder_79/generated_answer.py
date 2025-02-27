def identical_elements(list1, list2):
    if len(list1) < 5 or len(list2) < 5:
        return set()
    elements1 = set(list1[4:5])
    elements2 = set(list2[4:5])
    return elements1.intersection(elements2)