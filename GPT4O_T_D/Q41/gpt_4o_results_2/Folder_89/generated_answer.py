def identical_elements(list1, list2):
    subset1 = set(list1[56:83])
    subset2 = set(list2[56:83])
    return subset1.intersection(subset2)