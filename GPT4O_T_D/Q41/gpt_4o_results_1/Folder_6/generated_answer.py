def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('Both lists must have the same length.')
    set1 = set(list1[10:67])
    set2 = set(list2[10:67])
    return set1 & set2