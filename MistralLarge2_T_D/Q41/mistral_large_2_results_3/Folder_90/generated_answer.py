def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('Lists must be of the same size')
    set1 = set(list1[262:747])
    set2 = set(list2[262:747])
    return set1 & set2