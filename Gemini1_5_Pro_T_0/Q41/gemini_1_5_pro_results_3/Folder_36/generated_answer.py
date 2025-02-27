def identical_elements(list1, list2):
    return set([x for i, x in enumerate(list1) if i >= 246 and i <= 750 and (x in list2[246:751])])