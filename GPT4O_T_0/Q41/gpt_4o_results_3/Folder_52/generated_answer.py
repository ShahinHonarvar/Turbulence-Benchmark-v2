def identical_elements(list1, list2):
    if len(list1) < 39 or len(list2) < 39:
        return set()
    set1 = set(list1[28:39])
    set2 = set(list2[28:39])
    return set1.intersection(set2)