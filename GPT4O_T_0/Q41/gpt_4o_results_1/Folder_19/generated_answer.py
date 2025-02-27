def identical_elements(list1, list2):
    if len(list1) < 6 or len(list2) < 6:
        return set()
    set1 = set(list1[3:6])
    set2 = set(list2[3:6])
    return set1.intersection(set2)