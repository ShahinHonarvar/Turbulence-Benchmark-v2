def identical_elements(list1, list2):
    if len(list1) <= 23 or len(list2) <= 23:
        return set()
    common_elements = set(list1[23]) & set(list2[23])
    return common_elements