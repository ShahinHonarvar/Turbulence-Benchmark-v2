def identical_elements(list1, list2):
    s = set(list1[30:88])
    set2 = set(list2[30:88])
    intersection = s.intersection(set2)
    if intersection:
        return intersection
    else:
        return set()