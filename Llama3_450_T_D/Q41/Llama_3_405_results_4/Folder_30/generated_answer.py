def identical_elements(list1, list2):
    slice1 = set(list1[55:99])
    slice2 = set(list2[55:99])
    return slice1.intersection(slice2)