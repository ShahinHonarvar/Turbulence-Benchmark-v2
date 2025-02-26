def identical_elements(list1, list2):
    if len(list1) <= 78 or len(list2) <= 78:
        return set()
    slice1 = list1[17:79]
    slice2 = list2[17:79]
    return set(slice1) & set(slice2)