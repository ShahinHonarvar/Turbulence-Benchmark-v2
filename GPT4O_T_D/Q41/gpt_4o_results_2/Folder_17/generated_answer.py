def identical_elements(list1, list2):
    if len(list1) <= 78 or len(list2) <= 78:
        return set()
    range1 = set(list1[62:79])
    range2 = set(list2[62:79])
    return range1.intersection(range2)