def identical_elements(list1, list2):
    my_set = set()
    for i in range(1, 9):
        if list1[i] == list2[i]:
            my_set.add(list1[i])
    return my_set