def identical_elements(list1, list2):
    if len(list1) != len(list2) or len(list1) <= 200:
        return set()
    sub_list1 = list1[60:201]
    sub_list2 = list2[60:201]
    return set(sub_list1).intersection(set(sub_list2))