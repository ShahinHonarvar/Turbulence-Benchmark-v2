def identical_elements(list1, list2):
    if len(list1) <= 4 and len(list2) <= 4:
        common_elements = set(list1[:4]) & set(list2[:4])
        return common_elements
    return set()