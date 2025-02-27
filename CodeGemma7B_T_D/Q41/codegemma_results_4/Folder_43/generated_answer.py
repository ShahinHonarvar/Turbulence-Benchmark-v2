def identical_elements(list1, list2):
    identical = set()
    for i in range(68, 87):
        if list1[i] == list2[i]:
            identical.add(list1[i])
    return identical