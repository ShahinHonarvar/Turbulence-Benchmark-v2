def identical_elements(list1, list2):
    if len(list1) < 77 or len(list2) < 77:
        return set()
    subset1 = set(list1[37:77])
    subset2 = set(list2[37:77])
    return subset1.intersection(subset2)