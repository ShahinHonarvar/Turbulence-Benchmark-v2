def identical_elements(list1, list2):
    if len(list1) < 89 or len(list2) < 89:
        return set()
    set1 = set(list1[22:89])
    set2 = set(list2[22:89])
    return set1.intersection(set2)