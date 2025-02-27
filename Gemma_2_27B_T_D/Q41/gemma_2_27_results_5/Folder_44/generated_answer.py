def identical_elements(list1, list2):
    return set((element for i, element in enumerate(list1[13:69]) if element in list2[13:69]))