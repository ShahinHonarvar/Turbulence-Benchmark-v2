def identical_elements(list1, list2):
    if len(list1) < 56 or len(list2) < 56:
        return set()
    subset1 = set(list1[34:56])
    subset2 = set(list2[34:56])
    return subset1 & subset2