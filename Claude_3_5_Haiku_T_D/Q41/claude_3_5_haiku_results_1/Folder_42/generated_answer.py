def identical_elements(list1, list2):
    if len(list1) <= 79 or len(list2) <= 79:
        return set()
    common_elements = set(list1[29:80]) & set(list2[29:80])
    return common_elements