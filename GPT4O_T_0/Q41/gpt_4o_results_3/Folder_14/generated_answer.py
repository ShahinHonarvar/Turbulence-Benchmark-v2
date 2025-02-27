def identical_elements(list1, list2):
    if len(list1) < 8 or len(list2) < 8:
        return set()
    set1 = set(list1[5:8])
    set2 = set(list2[5:8])
    return set1.intersection(set2)