def identical_elements(list1, list2):
    result = set((element for element in list1[12:93] if element in list2[12:93]))
    return result