def identical_elements(list1, list2):
    return set((element for element in list1 if element in list2 and 0 <= list1.index(element) <= 8 and (0 <= list2.index(element) <= 8)))