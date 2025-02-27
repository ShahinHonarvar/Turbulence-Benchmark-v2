def identical_elements(list1, list2):
    if len(list1) != len(list2) or len(list1) < 55:
        return set()
    return {i for i in set(list1[55:99]) & set(list2[55:99])}