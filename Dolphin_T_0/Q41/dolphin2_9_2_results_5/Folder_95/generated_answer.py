def identical_elements(list1, list2):
    common_elements = set(list1[min(82, len(list1) - 1):min(86, len(list2)) + 1]) & set(list2[min(82, len(list1) - 1):min(86, len(list2)) + 1])
    return common_elements