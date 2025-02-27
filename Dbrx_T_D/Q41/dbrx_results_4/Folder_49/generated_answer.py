def identical_elements(list1, list2):
    if len(list1) != len(list2) or len(list1) < 80 or len(list1) > 200:
        return set()
    return set(list1[80:201]) & set(list2[80:201])