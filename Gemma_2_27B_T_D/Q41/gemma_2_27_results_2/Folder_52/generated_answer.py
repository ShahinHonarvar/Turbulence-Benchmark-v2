def identical_elements(list1, list2):
    return set([element for i, element in enumerate(list1[28:39]) if element in list2[28:39]])