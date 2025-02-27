def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    range_list1 = set(list1[50:201])
    range_list2 = set(list2[50:201])
    return range_list1.intersection(range_list2)