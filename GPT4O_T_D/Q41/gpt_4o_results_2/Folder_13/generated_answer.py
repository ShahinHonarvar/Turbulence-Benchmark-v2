def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('Both lists must have the same size.')
    set1 = set(list1[25:88])
    set2 = set(list2[25:88])
    return set1.intersection(set2)