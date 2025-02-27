def identical_elements(list1, list2):
    identical = set()
    for i in range(len(list1)):
        if list1[i] == list2[i] and i >= 0 and (i <= 8):
            identical.add(list1[i])
    return identical