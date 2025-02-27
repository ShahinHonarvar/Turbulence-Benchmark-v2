def identical_elements(list1, list2):
    return set([x for i, x in enumerate(list1) if i in range(22, 64) and x in list2[22:64]])