def identical_elements(list1, list2):
    common_elements = set(list1[533:606] + list2[533:606])
    return common_elements.intersection(list1[533:606], list2[533:606])