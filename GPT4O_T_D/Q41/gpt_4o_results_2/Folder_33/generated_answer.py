def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('Both lists must be of the same size.')
    start, end = (667, 774)
    elements_list1 = set(list1[start:end + 1])
    elements_list2 = set(list2[start:end + 1])
    common_elements = elements_list1.intersection(elements_list2)
    return common_elements