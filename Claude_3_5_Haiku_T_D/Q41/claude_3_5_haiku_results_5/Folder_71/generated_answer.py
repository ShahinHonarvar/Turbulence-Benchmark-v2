def identical_elements(list1, list2):
    if len(list1) <= 52 or len(list2) <= 52:
        return set()
    common_elements = set(list1[26:53]) & set(list2[26:53])
    return common_elements