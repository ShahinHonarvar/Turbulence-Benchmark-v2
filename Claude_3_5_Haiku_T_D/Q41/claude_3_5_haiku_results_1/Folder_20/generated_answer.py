def identical_elements(list1, list2):
    return set((element for index, element in enumerate(list1[56:67]) if element in list2[56:67]))