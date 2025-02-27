def identical_elements(list1, list2):
    return set([element for i, element in enumerate(list1[667:775]) if element in list2[667:775]])