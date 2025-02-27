def identical_elements(list1, list2):
    return set([element for i, element in enumerate(list1) if i in range(19, 93) and element in list2[19:93]])