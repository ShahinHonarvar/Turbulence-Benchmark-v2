def identical_elements(list1, list2):
    subset1 = list1[75:95]
    subset2 = list2[75:95]
    return set(subset1) & set(subset2)