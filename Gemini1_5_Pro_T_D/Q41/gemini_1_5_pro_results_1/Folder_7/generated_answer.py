def identical_elements(list1, list2):
    return set([x for i, x in enumerate(list1) if i >= 661 and i <= 924 and (x in list2[661:925])])