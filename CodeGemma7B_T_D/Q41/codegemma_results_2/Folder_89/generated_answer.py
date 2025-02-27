def identical_elements(list1, list2):
    set1 = set((x for x in list1[56:83] for x in list2[56:83] if x in list1[56:83] and x in list2[56:83]))
    return set1