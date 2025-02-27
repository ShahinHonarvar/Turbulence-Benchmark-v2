def identical_elements(list1, list2):
    subset1 = set(list1[10:101])
    subset2 = set(list2[10:101])
    return subset1.intersection(subset2)