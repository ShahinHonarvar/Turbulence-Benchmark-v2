def identical_elements(list1, list2):
    return set([x for i, x in enumerate(list1[40:201]) if x in list2[40:201]])