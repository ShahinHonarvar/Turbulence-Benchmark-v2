def identical_elements(list1, list2):
    identical_set = set()
    for i in range(62, 93):
        if list1[i] == list2[i]:
            identical_set.add(list1[i])
    return identical_set