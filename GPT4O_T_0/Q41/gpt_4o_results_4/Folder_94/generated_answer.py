def identical_elements(list1, list2):
    if len(list1) < 41 or len(list2) < 41:
        return set()
    set1 = set(list1[28:41])
    set2 = set(list2[28:41])
    return set1.intersection(set2)