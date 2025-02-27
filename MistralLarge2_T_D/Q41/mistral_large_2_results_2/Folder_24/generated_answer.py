def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    set1 = set(list1[74:96])
    set2 = set(list2[74:96])
    return set1 & set2