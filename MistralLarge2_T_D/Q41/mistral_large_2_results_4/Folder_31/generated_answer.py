def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('Both lists must be of the same size')
    set1 = set(list1[75:89])
    set2 = set(list2[75:89])
    return set1 & set2