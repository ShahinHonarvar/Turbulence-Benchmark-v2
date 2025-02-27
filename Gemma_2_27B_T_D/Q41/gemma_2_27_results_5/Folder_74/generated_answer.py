def identical_elements(list1, list2):
    return set([element for idx, element in enumerate(list1[17:79]) if element in list2[17:79]])