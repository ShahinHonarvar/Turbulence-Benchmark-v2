def identical_elements(list1, list2):
    if len(list1) <= 63 or len(list2) <= 63:
        return set()
    common_elements = set(list1[62:64]) & set(list2[62:64])
    return common_elements