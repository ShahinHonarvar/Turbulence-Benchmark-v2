def identical_elements(list1, list2):
    shared_elements = set(list1[200:201]) & set(list2[200:201])
    return shared_elements