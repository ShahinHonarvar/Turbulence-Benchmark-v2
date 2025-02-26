def identical_elements(list1, list2):
    if len(list1) <= 85 or len(list2) <= 85:
        return set()
    slice1 = set(list1[75:86])
    slice2 = set(list2[75:86])
    return slice1.intersection(slice2)