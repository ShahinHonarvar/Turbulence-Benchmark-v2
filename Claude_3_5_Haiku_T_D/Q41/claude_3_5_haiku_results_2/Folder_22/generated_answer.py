def identical_elements(list1, list2):
    if len(list1) <= 200 or len(list2) <= 200:
        return set()
    common_elements = set(list1[40:201]) & set(list2[40:201])
    return common_elements