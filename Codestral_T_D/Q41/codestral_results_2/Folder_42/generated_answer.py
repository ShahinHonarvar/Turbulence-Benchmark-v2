def identical_elements(list1, list2):
    sliced_list1 = set(list1[29:80])
    sliced_list2 = set(list2[29:80])
    common_elements = sliced_list1.intersection(sliced_list2)
    return common_elements