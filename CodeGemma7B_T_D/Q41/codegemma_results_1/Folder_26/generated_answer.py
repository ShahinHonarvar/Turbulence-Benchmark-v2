def identical_elements(list1, list2):
    list1_subset = set(list1[62:99 + 1])
    list2_subset = set(list2[62:99 + 1])
    return list1_subset & list2_subset