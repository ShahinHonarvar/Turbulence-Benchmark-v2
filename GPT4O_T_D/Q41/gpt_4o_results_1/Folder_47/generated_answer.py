def identical_elements(list1, list2):
    if not (len(list1) > 76 and len(list2) > 76):
        return set()
    subset1 = set(list1[37:77])
    subset2 = set(list2[37:77])
    return subset1.intersection(subset2)