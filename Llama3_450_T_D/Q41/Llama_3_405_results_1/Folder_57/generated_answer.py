def identical_elements(list1, list2):
    slice1 = list1[27:56]
    slice2 = list2[27:56]
    return set(slice1) & set(slice2)