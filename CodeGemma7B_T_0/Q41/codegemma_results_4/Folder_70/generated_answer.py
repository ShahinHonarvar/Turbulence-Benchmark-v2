def identical_elements(list1, list2):
    return set([x for x in list1[28:33] for y in list2[28:33] if x == y])