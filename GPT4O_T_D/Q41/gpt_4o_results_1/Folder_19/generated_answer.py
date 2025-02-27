def identical_elements(list1, list2):
    if len(list1) < 6 or len(list2) < 6:
        return set()
    sub_list1 = set(list1[3:6])
    sub_list2 = set(list2[3:6])
    return sub_list1.intersection(sub_list2)