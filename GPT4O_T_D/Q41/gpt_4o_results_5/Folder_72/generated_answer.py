def identical_elements(list1, list2):
    if len(list1) < 52 or len(list2) < 52:
        return set()
    subset1 = set(list1[29:52])
    subset2 = set(list2[29:52])
    return subset1.intersection(subset2)