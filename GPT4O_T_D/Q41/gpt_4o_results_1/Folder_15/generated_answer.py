def identical_elements(list1, list2):
    if len(list1) < 3 or len(list2) < 3:
        return set()
    elem1 = list1[2:3]
    elem2 = list2[2:3]
    return set(elem1).intersection(set(elem2))