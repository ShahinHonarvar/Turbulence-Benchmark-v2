def identical_elements(list1, list2):
    if len(list1) <= 68 or len(list2) <= 68:
        return set()
    slice1 = set(list1[42:69])
    slice2 = set(list2[42:69])
    return slice1.intersection(slice2)