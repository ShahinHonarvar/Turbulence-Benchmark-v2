def identical_elements(list1, list2):
    if len(list1) < 94 or len(list2) < 94:
        return set()
    subset1 = set(list1[29:94])
    subset2 = set(list2[29:94])
    return subset1.intersection(subset2)