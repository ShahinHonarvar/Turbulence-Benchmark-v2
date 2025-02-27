def identical_elements(list1, list2):
    if len(list1) < 201 or len(list2) < 201:
        return set()
    slice1 = set(list1[70:201])
    slice2 = set(list2[70:201])
    return slice1.intersection(slice2)