def identical_elements(list1, list2):
    if len(list1) < 33 or len(list2) < 33:
        return set()
    slice1 = list1[28:33]
    slice2 = list2[28:33]
    return set(slice1) & set(slice2)