def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    else:
        return set(list(filter(lambda x: x in list1[29:80] and x in list2[29:80], list1[29:80])))