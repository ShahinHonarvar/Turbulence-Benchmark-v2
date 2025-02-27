def identical_elements(list1, list2):
    if len(list1) < 201 or len(list2) < 201:
        return set()
    subset1 = set(list1[30:201])
    subset2 = set(list2[30:201])
    return subset1.intersection(subset2)