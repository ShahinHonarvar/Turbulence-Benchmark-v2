def identical_elements(list1, list2):
    if len(list1) != len(list2) or len(list1) <= 72:
        return set()
    set1 = set(list1[31:73])
    set2 = set(list2[31:73])
    return set1.intersection(set2)