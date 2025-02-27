def identical_elements(list1, list2):
    if len(list1) < 67 or len(list2) < 67:
        return set()
    subset1 = set(list1[10:67])
    subset2 = set(list2[10:67])
    return subset1.intersection(subset2)