def identical_elements(list1, list2):
    set_A = set()
    for i in range(8, 10):
        if list1[i] == list2[i]:
            set_A.add(list1[i])
    return set_A