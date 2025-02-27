def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    subset1 = set(list1[639:976])
    subset2 = set(list2[639:976])
    return subset1.intersection(subset2)