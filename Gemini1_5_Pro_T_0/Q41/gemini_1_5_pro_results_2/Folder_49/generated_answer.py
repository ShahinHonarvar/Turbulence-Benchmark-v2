def identical_elements(list1, list2):
    common_elements = set()
    for i in range(80, 201):
        if list1[i] in list2[80:201]:
            common_elements.add(list1[i])
    return common_elements