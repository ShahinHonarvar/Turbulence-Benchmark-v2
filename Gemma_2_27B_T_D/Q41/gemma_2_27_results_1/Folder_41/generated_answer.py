def identical_elements(list1, list2):
    return {element for i, element in enumerate(list1[6:7]) if element in list2[6:7]}