def identical_elements(list1, list2):
    slice1 = list1[22:51]
    slice2 = list2[22:51]
    return set(slice1) & set(slice2)