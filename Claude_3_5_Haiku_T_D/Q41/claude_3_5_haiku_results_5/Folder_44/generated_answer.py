def identical_elements(list1, list2):
    if len(list1) <= 68 or len(list2) <= 68:
        return set()
    slice1 = list1[13:69]
    slice2 = list2[13:69]
    set1 = set(slice1)
    set2 = set(slice2)
    return set1.intersection(set2)