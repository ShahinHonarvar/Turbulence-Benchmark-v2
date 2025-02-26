def identical_elements(list1, list2):
    if len(list1) <= 80 or len(list2) <= 80:
        return set()
    slice1 = set(list1[40:81])
    slice2 = set(list2[40:81])
    return slice1.intersection(slice2)