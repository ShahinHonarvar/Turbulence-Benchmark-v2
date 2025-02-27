def identical_elements(list1, list2):
    result_set = set()
    for i in range(533, 606):
        if list1[i] in list2 and list1[i] not in result_set:
            result_set.add(list1[i])
        if list2[i] in list1 and list2[i] not in result_set:
            result_set.add(list2[i])
    return result_set