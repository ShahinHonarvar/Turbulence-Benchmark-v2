def identical_elements(list1, list2):
    if len(list1) < 52 or len(list2) < 52:
        return set()
    sub_list1 = list1[29:52]
    sub_list2 = list2[29:52]
    return set(sub_list1).intersection(sub_list2)