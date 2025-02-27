def identical_elements(list1, list2):
    return set((element for i, element in enumerate(list1[:6]) if i < 6 and element in list2[:6]))