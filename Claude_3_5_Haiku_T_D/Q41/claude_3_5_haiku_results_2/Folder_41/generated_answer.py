def identical_elements(list1, list2):
    if len(list1) <= 6 or len(list2) <= 6:
        return set()
    common_elements = set(list1[6:7]) & set(list2[6:7])
    return common_elements