def identical_elements(list1, list2):
    set1 = set(list1[31:73]) if len(list1) > 31 else set()
    set2 = set(list2[31:73]) if len(list2) > 31 else set()
    return set1.intersection(set2)