def identical_elements(list1, list2):
    return set(list(filter(lambda x: x in list2[31:73], list1[31:73])))