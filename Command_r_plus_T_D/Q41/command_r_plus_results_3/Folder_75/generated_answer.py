def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('Both lists must be of the same size')
    common_elements = set(list1[56:58]) & set(list2[56:58])
    return common_elements