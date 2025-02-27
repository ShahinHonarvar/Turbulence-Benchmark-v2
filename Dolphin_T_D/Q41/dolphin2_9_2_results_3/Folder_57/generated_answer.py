def identical_elements(list1, list2):
    common_elements = set(list1[27:56]) & set(list2[27:56])
    return common_elements if common_elements else set()