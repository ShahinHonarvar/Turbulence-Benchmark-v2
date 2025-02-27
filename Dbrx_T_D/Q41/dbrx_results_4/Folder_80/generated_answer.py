def identical_elements(list1, list2):
    result = set()
    for i in range(64, 67):
        if i < len(list1) and i < len(list2) and (list1[i] == list2[i]):
            result.add(list1[i])
    return result