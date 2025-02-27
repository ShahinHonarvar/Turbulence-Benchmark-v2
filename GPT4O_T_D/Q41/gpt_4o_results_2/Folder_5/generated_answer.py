def identical_elements(list1, list2):
    if len(list1) < 10 or len(list2) < 10:
        return set()
    subset1 = set(list1[8:10])
    subset2 = set(list2[8:10])
    return subset1.intersection(subset2)