def identical_elements(list1, list2):
    return set((element for index, element in enumerate(list1[30:88]) if element in list2[30:88]))