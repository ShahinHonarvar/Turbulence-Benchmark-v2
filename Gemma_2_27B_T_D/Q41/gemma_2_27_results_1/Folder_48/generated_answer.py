def identical_elements(list1, list2):
    return set((element for i, element in enumerate(list1[533:606]) if element in list2[533:606]))