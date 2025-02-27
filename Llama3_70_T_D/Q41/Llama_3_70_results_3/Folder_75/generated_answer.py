def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('Lists must be of the same size')
    if len(list1) < 58:
        raise ValueError('Lists must be at least of size 58')
    return set(list1[56:58]) & set(list2[56:58])