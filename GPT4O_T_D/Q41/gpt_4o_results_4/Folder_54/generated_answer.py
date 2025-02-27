def identical_elements(list1, list2):
    if len(list1) <= 55 or len(list2) <= 55:
        return set()
    subset1 = set(list1[34:56])
    subset2 = set(list2[34:56])
    return subset1.intersection(subset2)