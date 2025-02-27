def identical_elements(list1, list2):
    if len(list1) <= 200 or len(list2) <= 200:
        return set()
    sub_list1 = list1[200:201]
    sub_list2 = list2[200:201]
    return set(sub_list1).intersection(sub_list2)