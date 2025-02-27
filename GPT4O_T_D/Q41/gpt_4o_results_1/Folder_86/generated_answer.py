def identical_elements(list1, list2):
    if len(list1) < 35 or len(list2) < 35:
        return set()
    set1 = set(list1[31:35])
    set2 = set(list2[31:35])
    return set1.intersection(set2)