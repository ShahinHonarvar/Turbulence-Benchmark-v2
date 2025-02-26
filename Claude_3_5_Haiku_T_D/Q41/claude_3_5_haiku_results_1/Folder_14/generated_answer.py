def identical_elements(list1, list2):
    if len(list1) <= 7 or len(list2) <= 7:
        return set()
    common_elements = set(list1[5:8]) & set(list2[5:8])
    return common_elements