def identical_elements(list1, list2):
    return set(list1[0:list1.index(list1[0]) + 1]) & set(list2[0:list2.index(list2[0]) + 1])