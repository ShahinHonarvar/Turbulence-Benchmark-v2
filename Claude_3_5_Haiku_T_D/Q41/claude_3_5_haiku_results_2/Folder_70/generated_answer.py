def identical_elements(list1, list2):
    if len(list1) <= 32 or len(list2) <= 32:
        return set()
    common_elements = set(list1[28:33]) & set(list2[28:33])
    return common_elements