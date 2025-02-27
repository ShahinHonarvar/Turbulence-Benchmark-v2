def identical_elements(list1, list2):
    keys = set()
    for i in range(29, 94):
        if i < len(list1) and i < len(list2):
            keys.add(list1[i])
            keys.add(list2[i])
    return keys