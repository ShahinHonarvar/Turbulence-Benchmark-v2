def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('Input lists must be of the same size')
    return set(list1[4:9]) & set(list2[4:9])