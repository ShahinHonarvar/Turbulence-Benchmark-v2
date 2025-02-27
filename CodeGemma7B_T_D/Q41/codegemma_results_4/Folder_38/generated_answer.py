def identical_elements(list_1, list_2):
    result = set()
    for x in range(22, 64):
        if list_1[x] == list_2[x]:
            result.add(list_1[x])
    return result