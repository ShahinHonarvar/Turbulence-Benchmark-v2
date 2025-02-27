def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    set1 = set(list1[17:79])
    set2 = set(list2[17:79])
    return set1 & set2