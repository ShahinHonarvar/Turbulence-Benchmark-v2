def identical_elements(list1, list2):
    common_elements = set(list1[0:3]) & set(list2[0:3])
    return common_elements