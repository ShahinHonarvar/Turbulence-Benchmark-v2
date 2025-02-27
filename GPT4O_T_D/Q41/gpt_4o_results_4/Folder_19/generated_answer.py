def identical_elements(list1, list2):
    subset1 = set(list1[3:6])
    subset2 = set(list2[3:6])
    return subset1.intersection(subset2)