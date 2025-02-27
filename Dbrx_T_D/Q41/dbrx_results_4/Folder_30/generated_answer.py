def identical_elements(list1, list2):
    return {i for i in set(list1[55:99]) & set(list2[55:99])} if len(list1) >= 99 and len(list2) >= 99 else {}