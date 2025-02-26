def identical_elements(list1, list2):
    if len(list1) <= 8 or len(list2) <= 8:
        return set()
    common_elements = set(list1[6:9]) & set(list2[6:9])
    return common_elements