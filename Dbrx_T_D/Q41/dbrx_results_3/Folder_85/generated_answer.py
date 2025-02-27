def identical_elements(list1, list2):
    result = set()
    for i in range(6, 9):
        if i in range(len(list1)) and i in range(len(list2)):
            if list1[i] == list2[i]:
                result.add(list1[i])
    return result