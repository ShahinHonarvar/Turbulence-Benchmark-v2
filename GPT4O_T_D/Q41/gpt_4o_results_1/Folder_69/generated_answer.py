def identical_elements(list1, list2):
    if len(list1) < 36 or len(list2) < 36:
        return set()
    set1 = set(list1[32:36])
    set2 = set(list2[32:36])
    return set1.intersection(set2)