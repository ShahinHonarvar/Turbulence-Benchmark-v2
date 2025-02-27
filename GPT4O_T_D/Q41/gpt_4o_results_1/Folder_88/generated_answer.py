def identical_elements(list1, list2):
    sub_list1 = list1[4:9]
    sub_list2 = list2[4:9]
    return set(sub_list1).intersection(set(sub_list2))