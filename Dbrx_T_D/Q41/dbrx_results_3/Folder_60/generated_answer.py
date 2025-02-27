def identical_elements(list1, list2):
    result = set()
    for i in range(75, 86):
        if list1[i] in list2 and list2[i] in list1:
            result.add(list1[i])
    return result