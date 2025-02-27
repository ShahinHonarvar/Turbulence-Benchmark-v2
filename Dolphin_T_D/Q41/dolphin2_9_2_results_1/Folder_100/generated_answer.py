def identical_elements(list1, list2):
    common_elements = []
    for i in range(42, 69):
        if i < len(list1) and i < len(list2):
            if list1[i] == list2[i]:
                common_elements.append(list1[i])
    return set(common_elements)