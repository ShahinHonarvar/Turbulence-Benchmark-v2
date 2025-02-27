def identical_elements(list1, list2):
    if len(list1) < 67 or len(list2) < 67:
        return set()
    sub_list1 = set(list1[64:67])
    sub_list2 = set(list2[64:67])
    return sub_list1.intersection(sub_list2)