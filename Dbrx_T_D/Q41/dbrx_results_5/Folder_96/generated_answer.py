def identical_elements(list1, list2):
    return set(filter(lambda x: list1.count(x) > 0 and list2.count(x) > 0, set(list1[50:201]) & set(list2[50:201])))