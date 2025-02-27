def identical_elements(list1, list2):
    return set((element for i, element in enumerate(list1[22:89]) if element in list2[22:89]))