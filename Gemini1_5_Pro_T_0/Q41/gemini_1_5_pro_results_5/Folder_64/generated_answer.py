def identical_elements(list1, list2):
    common_elements = set()
    for i in range(4):
        if i < len(list1) and list1[i] in list2[:4]:
            common_elements.add(list1[i])
    return common_elements