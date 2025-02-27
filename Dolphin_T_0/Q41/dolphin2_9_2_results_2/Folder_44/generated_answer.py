def identical_elements(list1, list2):
    set1 = set([i for i in list1[13:69] if i in list2[13:69]])
    return set1 if set1 else set()