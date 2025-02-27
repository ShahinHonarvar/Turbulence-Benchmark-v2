def identical_elements(list1, list2):
    subset1 = list1[209:557]
    subset2 = list2[209:557]
    return set(subset1).intersection(subset2)