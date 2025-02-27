def identical_elements(list1, list2):
    if len(list1) < 37 or len(list2) < 37:
        return set()
    set1 = set(list1[33:37])
    set2 = set(list2[33:37])
    return set1.intersection(set2)