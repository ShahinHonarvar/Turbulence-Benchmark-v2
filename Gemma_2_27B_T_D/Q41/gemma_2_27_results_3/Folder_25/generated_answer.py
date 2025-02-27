def identical_elements(list1, list2):
    return set([element for i, element in enumerate(list1[29:94]) if element in list2[29:94]])