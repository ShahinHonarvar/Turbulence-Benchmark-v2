def identical_elements(list1, list2):
    start, end = (33, 36)
    if len(list1) <= end or len(list2) <= end:
        return set()
    slice1 = set(list1[start:end + 1])
    slice2 = set(list2[start:end + 1])
    return slice1.intersection(slice2)