def identical_elements(list1, list2):
    return set((element for i, element in enumerate(list1[42:69]) if element in list2[42:69]))