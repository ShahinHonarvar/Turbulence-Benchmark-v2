def identical_elements(list1, list2):
    common_set = set(list1[667:775]) & set(list2[667:775])
    return common_set if common_set else set()