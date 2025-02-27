def identical_elements(list1, list2):
    if len(list1) < 35 or len(list2) < 35:
        return set()
    return set(list1[31:35]).intersection(list2[31:35])