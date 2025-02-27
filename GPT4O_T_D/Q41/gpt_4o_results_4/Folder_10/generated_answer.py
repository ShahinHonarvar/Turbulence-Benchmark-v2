def identical_elements(list1, list2):
    subset1 = set(list1[25:60])
    subset2 = set(list2[25:60])
    return subset1.intersection(subset2)