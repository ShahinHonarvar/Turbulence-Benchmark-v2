def identical_elements(list1, list2):
    shared_elements = set(list1[50:201]) & set(list2[50:201])
    return shared_elements