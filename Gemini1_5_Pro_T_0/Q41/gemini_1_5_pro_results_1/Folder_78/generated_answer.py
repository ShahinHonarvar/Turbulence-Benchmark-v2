def identical_elements(list1, list2):
    return set([x for i, x in enumerate(list1) if i >= 43 and i <= 51 and (x in list2[43:52])])