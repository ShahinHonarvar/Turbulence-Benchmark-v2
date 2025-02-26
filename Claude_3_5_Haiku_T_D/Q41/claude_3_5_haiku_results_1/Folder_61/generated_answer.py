def identical_elements(list1, list2):
    common_elements = set(list1[:7]) & set(list2[:7])
    return common_elements