def identical_elements(list_1, list_2):
    result = set()
    for i in range(80, 200 + 1, 1):
        if list_1[i] == list_2[i]:
            result.add(list_1[i])
    return result