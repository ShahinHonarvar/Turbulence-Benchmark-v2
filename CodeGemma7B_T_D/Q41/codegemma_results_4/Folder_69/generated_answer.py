def identical_elements(list1, list2):
    result_set = set()
    for i in range(32, 36):
        if list1[i] == list2[i]:
            result_set.add(list1[i])
    return result_set