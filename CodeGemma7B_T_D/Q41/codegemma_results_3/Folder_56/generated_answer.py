def identical_elements(list1, list2):
    result = set()
    for i in range(1, 9):
        if list1[i] in list2[i]:
            result.add(list1[i])
    return result