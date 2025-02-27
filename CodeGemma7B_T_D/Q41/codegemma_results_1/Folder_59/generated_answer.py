def identical_elements(list1, list2):
    result = set((element for element in list1 + list2 if element in list1 and element in list2))
    return result