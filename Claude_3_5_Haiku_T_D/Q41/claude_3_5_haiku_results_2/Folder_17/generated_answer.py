def identical_elements(list1, list2):
    if len(list1) <= 78 or len(list2) <= 78:
        return set()
    common_elements = set(list1[62:79]) & set(list2[62:79])
    return common_elements