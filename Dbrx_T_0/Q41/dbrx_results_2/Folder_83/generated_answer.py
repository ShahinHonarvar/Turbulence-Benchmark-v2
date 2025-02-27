def identical_elements(list1, list2):
    if len(list1) != len(list2) or len(list1) < 90 or len(list2) < 90:
        return set()
    return set(list1[90:201]) & set(list2[90:201])