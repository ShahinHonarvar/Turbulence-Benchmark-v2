def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    identical_set = set((el for el in list1[56:83] if el in list2[56:83]))
    return identical_set