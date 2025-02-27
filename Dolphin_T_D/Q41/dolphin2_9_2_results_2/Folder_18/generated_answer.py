def identical_elements(list1, list2):
    return set((element for element in set(list1[35:50]) if element in set(list2[35:50])))