def identical_elements(list1, list2):
    if len(list1) < 52 or len(list2) < 52:
        return set()
    set1 = set(list1[37:52])
    set2 = set(list2[37:52])
    return set1.intersection(set2)