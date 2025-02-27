def identical_elements(list1, list2):
    subset_list1 = set(list1[80:201])
    subset_list2 = set(list2[80:201])
    return subset_list1 & subset_list2