def identical_elements(list1, list2):
    if len(list1) <= 51 or len(list2) <= 51:
        return set()
    set1 = set(list1[29:52])
    set2 = set(list2[29:52])
    return set1.intersection(set2)