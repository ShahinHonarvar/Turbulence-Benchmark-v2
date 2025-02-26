def identical_elements(list1, list2):
    if len(list1) <= 97 or len(list2) <= 97:
        return set()
    common_elements = set(list1[21:98]) & set(list2[21:98])
    return common_elements