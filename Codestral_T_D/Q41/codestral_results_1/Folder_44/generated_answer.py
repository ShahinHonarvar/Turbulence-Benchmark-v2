def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('Both lists should be of the same size')
    if len(list1) <= 68:
        raise ValueError('Lists should have at least 69 elements')
    return set(list1[13:69]) & set(list2[13:69])