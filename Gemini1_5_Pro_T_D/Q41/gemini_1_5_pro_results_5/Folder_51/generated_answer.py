def identical_elements(list1, list2):
    common_elements = set()
    for i in range(0, 3):
        if list1[i] in list2[:3]:
            common_elements.add(list1[i])
    return common_elements