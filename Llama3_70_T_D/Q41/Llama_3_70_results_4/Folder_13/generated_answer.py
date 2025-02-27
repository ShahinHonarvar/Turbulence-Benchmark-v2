def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('Lists must be of the same size')
    if len(list1) < 88:
        raise ValueError('Lists must have at least 88 elements')
    set1 = set(list1[25:88])
    set2 = set(list2[25:88])
    return set1.intersection(set2)