def identical_elements(list1, list2):
    return set([element for i, element in enumerate(list1[91:100]) if element in list2[91:100]])