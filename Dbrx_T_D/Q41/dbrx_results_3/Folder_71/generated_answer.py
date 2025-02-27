def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    return {list1[i] for i in range(26, 53) if list1[i] == list2[i] and list1[i] not in list1[:26] and (list1[i] not in list1[53:])}