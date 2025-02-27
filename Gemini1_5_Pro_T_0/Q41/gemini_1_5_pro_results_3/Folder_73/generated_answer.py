def identical_elements(list1, list2):
    return set([x for i, x in enumerate(list1) if i >= 19 and i <= 92 and (x in list2[19:93])])