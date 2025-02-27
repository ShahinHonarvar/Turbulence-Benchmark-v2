def identical_elements(list1, list2):
    return set((element for i in range(5) if element in list1[:5] and element in list2[:5]))