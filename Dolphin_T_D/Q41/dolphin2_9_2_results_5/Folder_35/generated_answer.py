def identical_elements(list1, list2):
    common_elements = set()
    for i in range(30, 49):
        if i < len(list1) and i < len(list2):
            common_elements.add(list1[i])
            common_elements.add(list2[i])
    return common_elements