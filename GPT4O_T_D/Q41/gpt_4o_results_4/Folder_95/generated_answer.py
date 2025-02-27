def identical_elements(list1, list2):
    elements_list1 = set(list1[82:87])
    elements_list2 = set(list2[82:87])
    return elements_list1.intersection(elements_list2)