def identical_elements(list1, list2):
    return set([x for x in list1[14:65] for y in list2[14:65] if x == y])