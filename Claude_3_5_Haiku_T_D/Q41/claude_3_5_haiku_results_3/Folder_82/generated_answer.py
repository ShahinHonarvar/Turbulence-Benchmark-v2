def identical_elements(list1, list2):
    if len(list1) <= 200 or len(list2) <= 200:
        return set()
    slice1 = list1[20:201]
    slice2 = list2[20:201]
    common_elements = set(slice1) & set(slice2)
    return common_elements