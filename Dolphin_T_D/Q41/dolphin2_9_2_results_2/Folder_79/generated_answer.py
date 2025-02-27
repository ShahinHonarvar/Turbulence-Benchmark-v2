def identical_elements(list1, list2):
    identical_set = set()
    for i in range(4, 5):
        if list1[i] in list2:
            identical_set.add(list1[i])
    return identical_set