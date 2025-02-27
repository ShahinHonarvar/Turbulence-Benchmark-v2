def identical_elements(list1, list2):
    index_range = slice(23, 24)
    set1 = set(list1[index_range])
    set2 = set(list2[index_range])
    return set1 & set2