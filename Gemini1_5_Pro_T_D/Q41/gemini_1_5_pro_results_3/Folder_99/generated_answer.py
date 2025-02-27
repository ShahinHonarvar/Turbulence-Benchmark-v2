def identical_elements(list1, list2):
    common_elements = set()
    for i in range(310, 371):
        if list1[i] in list2[310:371]:
            common_elements.add(list1[i])
    return common_elements