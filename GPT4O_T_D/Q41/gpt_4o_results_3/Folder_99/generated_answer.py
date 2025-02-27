def identical_elements(list1, list2):
    range1 = set(list1[310:371])
    range2 = set(list2[310:371])
    return range1.intersection(range2)