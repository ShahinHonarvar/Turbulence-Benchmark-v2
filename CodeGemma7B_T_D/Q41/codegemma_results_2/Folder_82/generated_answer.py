def identical_elements(list1, list2):
    return set([x for x in list1[20:201] for y in list2[20:201] if x == y])