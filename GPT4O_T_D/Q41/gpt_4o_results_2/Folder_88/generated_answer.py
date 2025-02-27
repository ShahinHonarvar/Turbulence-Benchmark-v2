def identical_elements(list1, list2):
    subset1 = list1[4:9]
    subset2 = list2[4:9]
    common_elements = set(subset1).intersection(set(subset2))
    return common_elements