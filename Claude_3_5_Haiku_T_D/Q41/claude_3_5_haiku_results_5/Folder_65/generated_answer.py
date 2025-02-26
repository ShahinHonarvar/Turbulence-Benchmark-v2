def identical_elements(list1, list2):
    if len(list1) <= 98 or len(list2) <= 98:
        return set()
    common_elements = set(list1[56:99]) & set(list2[56:99])
    return common_elements