def identical_elements(list1, list2):
    subset1 = set(list1[310:371])
    subset2 = set(list2[310:371])
    return subset1.intersection(subset2)