def identical_elements(list1, list2):
    if len(list1) < 81 or len(list2) < 81:
        return set()
    sub_list1 = list1[40:81]
    sub_list2 = list2[40:81]
    return set(sub_list1) & set(sub_list2)