def identical_elements(list_1, list_2):
    identical_set = set()
    for i in range(26, 54):
        if list_1[i] == list_2[i]:
            identical_set.add(list_1[i])
    return identical_set