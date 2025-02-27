def identical_elements(list_1, list_2):
    res = set()
    for i in range(7):
        if list_1[i] == list_2[i]:
            res.add(list_1[i])
    return res