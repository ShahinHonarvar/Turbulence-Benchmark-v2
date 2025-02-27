def identical_elements(list1, list2):
    range1 = set(list1[:5])
    range2 = set(list2[:5])
    return range1.intersection(range2)