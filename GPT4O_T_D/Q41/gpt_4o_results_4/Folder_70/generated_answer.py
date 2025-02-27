def identical_elements(list1, list2):
    if len(list1) < 33 or len(list2) < 33:
        return set()
    subset1 = set(list1[28:33])
    subset2 = set(list2[28:33])
    return subset1.intersection(subset2)