def identical_elements(list1, list2):
    index_limit = 9
    set1 = set(list1[:index_limit])
    set2 = set(list2[:index_limit])
    return set1 & set2