def identical_elements(list1, list2):
    if len(list1) <= 68 or len(list2) <= 68:
        return set()
    slice1 = list1[42:69]
    slice2 = list2[42:69]
    return set(slice1) & set(slice2)