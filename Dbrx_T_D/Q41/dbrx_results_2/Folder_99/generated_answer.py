def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    result = set()
    for i in range(310, 371):
        if list1[i] in list2 and list2.index(list1[i]) >= 310 and (list2.index(list1[i]) <= 370):
            result.add(list1[i])
        elif list2[i] in list1 and list1.index(list2[i]) >= 310 and (list1.index(list2[i]) <= 370):
            result.add(list2[i])
    return result