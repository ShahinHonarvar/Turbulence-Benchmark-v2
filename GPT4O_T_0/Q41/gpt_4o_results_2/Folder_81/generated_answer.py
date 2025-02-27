def identical_elements(list1, list2):
    if len(list1) < 101 or len(list2) < 101:
        return set()
    set1 = set(list1[10:101])
    set2 = set(list2[10:101])
    return set1.intersection(set2)