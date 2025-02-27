def identical_elements(list1, list2):
    return {element for i in range(5, 8) if i < len(list1) and i < len(list2) and (list1[i] == list2[i])}