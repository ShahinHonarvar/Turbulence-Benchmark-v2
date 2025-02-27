def identical_elements(list1, list2):
    if len(list1) < 51 or len(list2) < 51:
        return set()
    slice1 = list1[22:51]
    slice2 = list2[22:51]
    return set(slice1).intersection(slice2)