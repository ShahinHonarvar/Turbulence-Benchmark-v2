def identical_elements(list1, list2):
    return set([x for i, x in enumerate(list1[29:80]) if x in list2[29:80]])