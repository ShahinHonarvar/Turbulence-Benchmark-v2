def identical_elements(list1, list2):
    set_result = set()
    for i in range(25, 88):
        if i < len(list1) and i < len(list2):
            if list1[i] == list2[i]:
                set_result.add(list1[i])
    return set_result