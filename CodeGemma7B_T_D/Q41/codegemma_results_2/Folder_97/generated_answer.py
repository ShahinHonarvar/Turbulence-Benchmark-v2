def identical_elements(list1, list2):
    new_list = set()
    for i in range(40, 81):
        if list1[i] in list2 and list2[i] in list1:
            new_list.add(list1[i])
    return new_list