def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('Lists must be of the same size')
    if len(list1) < 24:
        raise ValueError('Lists must contain at least 24 elements')
    return set(list1[23:24]) & set(list2[23:24])