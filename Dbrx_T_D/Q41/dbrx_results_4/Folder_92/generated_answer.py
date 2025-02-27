def identical_elements(list1, list2):
    return set(list1[0]) & set(list2[0]) | set(list1[0:1]) & set(list2[0:1])