def identical_elements(list1, list2):
    subset1 = list1[62:100]
    subset2 = list2[62:100]
    return set(subset1).intersection(subset2)