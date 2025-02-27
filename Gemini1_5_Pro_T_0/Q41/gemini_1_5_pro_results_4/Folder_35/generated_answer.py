def identical_elements(list1, list2):
    return set([x for i, x in enumerate(list1) if i >= 30 and i <= 48 and (x in list2[30:49])])