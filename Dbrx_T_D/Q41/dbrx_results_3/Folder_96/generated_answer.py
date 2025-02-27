def identical_elements(list1, list2):
    if len(list1) != len(list2) or len(list1) < 51 or len(list1) > 200:
        return set()
    return set(list1[50:201]) & set(list2[50:201])