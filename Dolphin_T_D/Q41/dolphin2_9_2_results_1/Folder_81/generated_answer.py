def identical_elements(list1, list2):
    subset1 = set(list1[10:100])
    subset2 = set(list2[10:100])
    return subset1.intersection(subset2)