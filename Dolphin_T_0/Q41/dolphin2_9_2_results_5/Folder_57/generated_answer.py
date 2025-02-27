def identical_elements(list1, list2):
    common_elements = {i for i in set(list1[27:56]) if i in list2[27:56]}
    return common_elements