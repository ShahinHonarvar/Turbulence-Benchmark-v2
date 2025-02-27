def identical_elements(list1, list2):
    slice1 = list1[23:24]
    slice2 = list2[23:24]
    return set(slice1) & set(slice2)