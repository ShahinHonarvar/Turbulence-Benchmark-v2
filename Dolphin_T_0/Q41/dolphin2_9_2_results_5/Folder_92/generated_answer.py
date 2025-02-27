def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('Both lists must have the same size')
    return set(list1[0:1]) & set(list2[0:1])