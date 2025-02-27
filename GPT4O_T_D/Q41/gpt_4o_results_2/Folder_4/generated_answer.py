def identical_elements(list1, list2):
    if len(list1) != len(list2) or len(list1) < 93:
        return set()
    set1 = set(list1[12:93])
    set2 = set(list2[12:93])
    return set1.intersection(set2)