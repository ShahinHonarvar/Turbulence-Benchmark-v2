def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('Lists must be the same size')
    set1 = set(list1[:2])
    set2 = set(list2[:2])
    return set1 & set2