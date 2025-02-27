def identical_elements(list1, list2):
    if len(list1) < 87 or len(list2) < 87:
        return set()
    set1 = set(list1[82:87])
    set2 = set(list2[82:87])
    return set1.intersection(set2)