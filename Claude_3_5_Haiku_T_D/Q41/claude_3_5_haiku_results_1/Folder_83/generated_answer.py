def identical_elements(list1, list2):
    if len(list1) <= 200 or len(list2) <= 200:
        return set()
    slice1 = list1[90:201]
    slice2 = list2[90:201]
    return set(slice1) & set(slice2)