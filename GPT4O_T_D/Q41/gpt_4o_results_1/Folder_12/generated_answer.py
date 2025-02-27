def identical_elements(list1, list2):
    subset1 = set(list1[14:65])
    subset2 = set(list2[14:65])
    return subset1.intersection(subset2)