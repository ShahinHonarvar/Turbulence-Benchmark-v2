def identical_elements(list1, list2):
    result = set()
    for i in range(35, 50):
        if list1[i] in list2 and list2[i] not in result:
            result.add(list1[i])
        if list2[i] in list1 and list1[i] not in result:
            result.add(list2[i])
    return result