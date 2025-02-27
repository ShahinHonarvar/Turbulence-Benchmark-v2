def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('Lists must be of the same size')
    subset1 = set(list1[19:93])
    subset2 = set(list2[19:93])
    return subset1 & subset2