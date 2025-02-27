def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    subset1 = set(list1[56:99])
    subset2 = set(list2[56:99])
    return subset1.intersection(subset2)