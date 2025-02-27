def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('Both lists must have the same size')
    set1 = set(list1[5:8])
    set2 = set(list2[5:8])
    return set1.intersection(set2)