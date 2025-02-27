def identical_elements(list1, list2):
    subset1 = set(list1[22:51])
    subset2 = set(list2[22:51])
    return subset1.intersection(subset2)