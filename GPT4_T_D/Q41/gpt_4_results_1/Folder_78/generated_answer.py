def identical_elements(list1, list2):
    slice1 = set(list1[43:52])
    slice2 = set(list2[43:52])
    return slice1.intersection(slice2)