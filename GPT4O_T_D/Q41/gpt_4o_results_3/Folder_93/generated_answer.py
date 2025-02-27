def identical_elements(list1, list2):
    if len(list1) < 95 or len(list2) < 95:
        return set()
    subset1 = set(list1[75:95])
    subset2 = set(list2[75:95])
    return subset1.intersection(subset2)