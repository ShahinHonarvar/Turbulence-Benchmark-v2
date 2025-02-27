def identical_elements(list1, list2):
    slice1 = list1[5:8]
    slice2 = list2[5:8]
    return set(slice1) & set(slice2)