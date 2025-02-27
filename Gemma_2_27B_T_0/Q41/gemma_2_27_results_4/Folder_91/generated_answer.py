def identical_elements(list1, list2):
    return set((element for i, element in enumerate(list1[:5]) if element in list2[:5]))