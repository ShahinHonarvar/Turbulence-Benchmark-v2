def identical_elements(list1, list2):
    return set([x for i, x in enumerate(list1[13:69]) if x in list2[13:69]])