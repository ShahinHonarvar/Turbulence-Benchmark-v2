def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('Both lists must be of the same size')
    common_elements = set(list1[50:55]) & set(list2[50:55])
    return common_elements