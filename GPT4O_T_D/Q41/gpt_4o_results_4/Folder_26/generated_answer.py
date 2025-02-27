def identical_elements(list1, list2):
    index_start = 62
    index_end = 99
    set1 = set(list1[index_start:index_end + 1])
    set2 = set(list2[index_start:index_end + 1])
    return set1 & set2