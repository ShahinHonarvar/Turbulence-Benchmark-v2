def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('Both lists must be of the same size.')
    common_elements = set(list1[8:10]) & set(list2[8:10])
    return common_elements