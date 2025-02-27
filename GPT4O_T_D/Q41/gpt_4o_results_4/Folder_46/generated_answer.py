def identical_elements(list1, list2):
    slice1 = set(list1[30:88])
    slice2 = set(list2[30:88])
    return slice1.intersection(slice2)