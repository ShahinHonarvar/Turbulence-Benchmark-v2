def identical_elements(list1, list2):
    slice1 = list1[686:988]
    slice2 = list2[686:988]
    return set(slice1).intersection(slice2)