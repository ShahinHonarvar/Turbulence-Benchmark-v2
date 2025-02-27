def identical_elements(list1, list2):
    if len(list1) < 49 or len(list2) < 49:
        return set()
    set1 = set(list1[30:49])
    set2 = set(list2[30:49])
    return set1.intersection(set2)