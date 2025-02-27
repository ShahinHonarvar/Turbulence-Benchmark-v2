def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('Both lists must have the same size')
    if len(list1) < 58:
        raise ValueError('Both lists must have at least 58 elements')
    return set(list1[56:58]) & set(list2[56:58])