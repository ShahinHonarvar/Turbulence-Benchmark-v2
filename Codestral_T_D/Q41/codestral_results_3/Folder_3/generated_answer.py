def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('Both lists should have the same size.')
    if len(list1) < 92 or len(list2) < 92:
        raise ValueError('Both lists should have at least 92 elements.')
    return set(list1[62:93]).intersection(set(list2[62:93]))