def identical_elements(list1, list2):
    index_start = 21
    index_end = 97
    set1 = set(list1[index_start:index_end + 1])
    set2 = set(list2[index_start:index_end + 1])
    return set1.intersection(set2)