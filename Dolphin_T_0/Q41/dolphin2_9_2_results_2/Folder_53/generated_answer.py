def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    return set(list1[200:201]) & set(list2[200:201])