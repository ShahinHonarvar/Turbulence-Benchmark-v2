def identical_elements(list1, list2):
    return set([element for i, element in enumerate(list1) if i in range(9, 10) and element in list2[9:10]])