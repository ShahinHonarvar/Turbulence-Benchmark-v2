def identical_elements(list1, list2):
    identical_elements_set = set()
    for i in range(310, 371):
        if list1[i] == list2[i]:
            identical_elements_set.add(list1[i])
    return identical_elements_set