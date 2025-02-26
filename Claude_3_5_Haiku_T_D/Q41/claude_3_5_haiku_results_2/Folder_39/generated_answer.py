def identical_elements(list1, list2):
    if len(list1) <= 30 or len(list2) <= 30:
        return set()
    common_elements = set(list1[20:31]) & set(list2[20:31])
    return common_elements