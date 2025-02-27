def identical_elements(list1, list2):
    identical = set()
    for i in range(527, 539):
        if list1[i] in list2[i]:
            identical.add(list1[i])
    return identical