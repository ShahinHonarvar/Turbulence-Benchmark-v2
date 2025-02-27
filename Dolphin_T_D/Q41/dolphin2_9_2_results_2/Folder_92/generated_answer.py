def identical_elements(list1, list2):
    set_common = set(list1[0:index + 1])
    set_common = set_common.intersection(set(list2[0:index + 1]))
    return set_common