def identical_elements(list1, list2):
    set1 = set((element for element in list1[75:86] if element in list2[75:86]))
    return set1 or set()