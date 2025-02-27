def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    subset1 = set(list1[50:201])
    subset2 = set(list2[50:201])
    return subset1.intersection(subset2)