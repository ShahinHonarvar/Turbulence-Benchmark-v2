def identical_elements(list1, list2):
    if len(list1) <= 100 or len(list2) <= 100:
        return set()
    common_elements = set(list1[10:101]) & set(list2[10:101])
    return common_elements