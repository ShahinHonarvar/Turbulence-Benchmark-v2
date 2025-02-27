def identical_elements(list1, list2):
    subset1 = set(list1[75:86])
    subset2 = set(list2[75:86])
    return subset1.intersection(subset2)