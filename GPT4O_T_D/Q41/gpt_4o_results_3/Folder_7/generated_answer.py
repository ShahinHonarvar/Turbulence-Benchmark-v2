def identical_elements(list1, list2):
    subset_list1 = list1[661:925]
    subset_list2 = list2[661:925]
    return set(subset_list1).intersection(subset_list2)