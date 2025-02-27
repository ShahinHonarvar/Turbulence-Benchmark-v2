def identical_elements(list1, list2):
    if len(list1) < 33 or len(list2) < 33:
        return set()
    set1 = set(list1[28:33])
    set2 = set(list2[28:33])
    return set1.intersection(set2)