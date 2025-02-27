def identical_elements(list1, list2):
    return set((element for element in list1[1:9] if element in list2[1:9]))