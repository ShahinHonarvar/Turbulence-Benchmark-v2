def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    return set((el for el in list1[29:94] if el in list2[29:94]))