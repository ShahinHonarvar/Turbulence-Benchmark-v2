def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('Both lists must have the same size')
    elements_in_range1 = set(list1[59:98])
    elements_in_range2 = set(list2[59:98])
    return elements_in_range1.intersection(elements_in_range2)