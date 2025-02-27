def identical_elements(list1, list2):
    return set(filter(lambda x: list1.count(x) > 0 and list2.count(x) > 0, list1[37:77] + list2[37:77]))