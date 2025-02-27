def identical_elements(list1, list2):
    return {element for i, element in enumerate(list1[50:55]) if element in list2[50:55]}