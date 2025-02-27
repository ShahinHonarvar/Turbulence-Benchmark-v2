def identical_elements(list1, list2):
    if len(list1) != len(list2) or len(list1) < 557:
        return set()
    subset1 = set(list1[209:557])
    subset2 = set(list2[209:557])
    return subset1.intersection(subset2)