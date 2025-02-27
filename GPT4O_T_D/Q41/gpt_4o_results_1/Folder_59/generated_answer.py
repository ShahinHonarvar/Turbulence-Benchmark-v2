def identical_elements(list1, list2):
    check_index = min(9, len(list1), len(list2))
    set1 = set(list1[:check_index])
    set2 = set(list2[:check_index])
    return set1 & set2