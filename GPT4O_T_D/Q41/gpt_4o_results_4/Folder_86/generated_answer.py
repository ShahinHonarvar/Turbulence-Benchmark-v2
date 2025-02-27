def identical_elements(list1, list2):
    return set(list1[31:35]) & set(list2[31:35]) if len(list1) > 34 and len(list2) > 34 else set()