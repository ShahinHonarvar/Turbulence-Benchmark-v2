def identical_elements(list1, list2):
    start_index, end_index = (667, 774)
    set1 = set(list1[start_index:end_index + 1])
    set2 = set(list2[start_index:end_index + 1])
    return set1.intersection(set2)