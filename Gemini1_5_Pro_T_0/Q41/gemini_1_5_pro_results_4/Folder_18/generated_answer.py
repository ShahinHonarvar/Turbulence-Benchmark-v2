def identical_elements(list1, list2):
    common_elements = set()
    for i in range(35, 50):
        if list1[i] in list2[35:50]:
            common_elements.add(list1[i])
    return common_elements