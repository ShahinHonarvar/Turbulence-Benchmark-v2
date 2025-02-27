def identical_elements(list1, list2):
    return set((element for i, element in enumerate(list1[10:101]) if element in list2[10:101]))