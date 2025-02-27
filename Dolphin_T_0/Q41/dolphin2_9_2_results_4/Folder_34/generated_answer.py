def identical_elements(list1, list2):
    return set((element for i in range(60, 201) for element in [list1[i - 1], list2[i - 1]] if element in list1[i - 1:i] and element in list2[i - 1:i]))