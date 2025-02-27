def identical_elements(list1, list2):
    return set([x for i, x in enumerate(list1) if i >= 639 and i <= 975 and (x in list2[639:976])])