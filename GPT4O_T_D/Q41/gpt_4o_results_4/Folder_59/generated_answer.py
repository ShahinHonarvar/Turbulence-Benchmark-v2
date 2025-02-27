def identical_elements(list1, list2):
    range_limit = 9
    result_set = set(list1[:range_limit]) & set(list2[:range_limit])
    return result_set