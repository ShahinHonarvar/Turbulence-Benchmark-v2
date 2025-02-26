def identical_elements(list1, list2):
    return set((element for i, element in enumerate(list1) if 55 <= i <= 98 and element in list2[55:99]))