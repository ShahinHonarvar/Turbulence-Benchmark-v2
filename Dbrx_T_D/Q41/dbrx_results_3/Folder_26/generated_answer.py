def identical_elements(list1, list2):
    return set(list(filter(lambda x: list1.count(x) > 0 and list2.count(x) > 0, list1[62:100] + list2[62:100])))