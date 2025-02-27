def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    return {elem for elem in set(list1[667:775]) & set(list2[667:775])}