def identical_elements(list1, list2):
    return set([x for i, x in enumerate(list1) if i >= 37 and i <= 76 and (x in list2[37:77])])