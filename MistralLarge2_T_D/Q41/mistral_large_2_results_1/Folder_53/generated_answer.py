def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('Lists must be of the same size')
    set1 = set(list1[200:201])
    set2 = set(list2[200:201])
    return set1.intersection(set2)