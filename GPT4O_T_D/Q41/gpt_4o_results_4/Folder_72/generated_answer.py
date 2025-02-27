def identical_elements(list1, list2):
    if len(list1) < 52 or len(list2) < 52:
        return set()
    sub_list1 = set(list1[29:52])
    sub_list2 = set(list2[29:52])
    return sub_list1.intersection(sub_list2)