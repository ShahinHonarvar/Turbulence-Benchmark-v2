def identical_elements(list1, list2):
    return set((element for i, element in enumerate(list1) if 13 <= i <= 68 and element in list2[13:69]))