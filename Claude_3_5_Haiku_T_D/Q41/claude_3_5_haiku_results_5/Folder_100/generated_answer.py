def identical_elements(list1, list2):
    if len(list1) <= 68 or len(list2) <= 68:
        return set()
    common_elements = set(list1[42:69]) & set(list2[42:69])
    return common_elements