def identical_elements(list1, list2):
    result = set()
    for i in range(91, 100):
        if list1[i] in list2[i] and list1[i] not in result:
            result.add(list1[i])
    return result if len(result) > 0 else {None}