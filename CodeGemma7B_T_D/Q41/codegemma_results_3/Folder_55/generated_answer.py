def identical_elements(list1, list2):
    result = set()
    for i in range(9, len(list1)):
        if list1[i] in result:
            result.add(list1[i])
        elif list1[i] in list2[i] and list2[i] not in result:
            result.add(list1[i])
    return result