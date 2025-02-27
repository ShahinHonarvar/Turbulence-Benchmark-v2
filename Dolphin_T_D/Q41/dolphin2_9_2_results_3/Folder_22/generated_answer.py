def identical_elements(list1, list2):
    elements = set(list1[40:201] + list2[40:201])
    common_elements = {element for element in elements if element in list1[40:201] and element in list2[40:201]}
    return common_elements