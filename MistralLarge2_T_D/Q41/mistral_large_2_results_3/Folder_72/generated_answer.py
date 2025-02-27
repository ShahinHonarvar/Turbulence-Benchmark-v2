def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('Both lists must have the same size')
    set1 = set(list1[29:52])
    set2 = set(list2[29:52])
    return set1 & set2