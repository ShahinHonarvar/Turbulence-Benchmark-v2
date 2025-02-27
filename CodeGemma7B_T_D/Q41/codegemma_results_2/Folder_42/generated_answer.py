def identical_elements(list_1, list_2):
    result = set()
    if len(list_1) != len(list_2):
        return result
    for i in range(29, 80):
        if list_1[i] == list_2[i]:
            result.add(list_1[i])
    return result or set()