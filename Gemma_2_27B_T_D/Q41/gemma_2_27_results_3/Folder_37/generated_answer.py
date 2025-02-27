def identical_elements(list1, list2):
    return set([element for i, element in enumerate(list1) if i in range(1, 6) and element in list2[1:6]])