def identical_elements(list1, list2):
    sub_list1 = list1[40:201]
    sub_list2 = list2[40:201]
    return set(sub_list1).intersection(sub_list2)