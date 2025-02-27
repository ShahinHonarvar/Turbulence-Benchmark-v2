def identical_elements(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list) or len(list1) != len(list2):
        return set()
    result = set()
    for i in range(len(list1)):
        if 75 <= i <= 85:
            for j in range(len(list1[i])):
                if list1[i][j] == list2[i][j]:
                    result.add(list1[i][j])
    return result