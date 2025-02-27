def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('Both lists should have the same size')
    return set(list1[262:747]) & set(list2[262:747])