def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    result = set()
    for i in range(4, 9):
        if list1[i] in list2[4:9] and list1[i] not in result:
            result.add(list1[i])
    return result