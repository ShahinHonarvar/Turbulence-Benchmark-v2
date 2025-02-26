def identical_elements(list1, list2):
    if len(list1) <= 35 or len(list2) <= 35:
        return set()
    common_elements = set(list1[32:36]) & set(list2[32:36])
    return common_elements