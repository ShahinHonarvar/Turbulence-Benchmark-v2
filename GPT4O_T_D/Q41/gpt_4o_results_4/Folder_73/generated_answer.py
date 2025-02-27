def identical_elements(list1, list2):
    sub_list1 = list1[19:93]
    sub_list2 = list2[19:93]
    return set(sub_list1).intersection(sub_list2)