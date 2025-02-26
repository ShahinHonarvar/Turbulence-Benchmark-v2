def identical_elements(list1, list2):
    return set((element for i in range(56, 58) for element in [list1[i], list2[i]] if element in list1[56:58] and element in list2[56:58]))